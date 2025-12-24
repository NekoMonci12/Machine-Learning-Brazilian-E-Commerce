import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    customers = pd.read_csv("dataset/olist_customers_dataset.csv")
    orders = pd.read_csv("dataset/olist_orders_dataset.csv")
    order_payments = pd.read_csv("dataset/olist_order_payments_dataset.csv")
    order_reviews = pd.read_csv("dataset/olist_order_reviews_dataset.csv")
    return customers, orders, order_payments, order_reviews

def customers_vs_revenue_per_state(customers, orders, payments):
    df = (
        orders.merge(customers, on="customer_id")
        .merge(payments, on="order_id")
    )

    state_summary = (
        df.groupby("customer_state")
        .agg(
            total_customers=("customer_id", "nunique"),
            total_revenue=("payment_value", "sum")
        )
        .reset_index()
        .sort_values("total_customers", ascending=False)
    )
    return state_summary

def prepare_delivery_review_df(orders, reviews):
    df = orders.merge(reviews, on="order_id")
    df = df.dropna(subset=["order_delivered_customer_date"])

    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])

    df["delivery_time_days"] = (
        df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
    ).dt.days

    return df[df["delivery_time_days"] >= 0]

st.set_page_config(page_title="Olist E-Commerce Analysis", layout="wide")
st.title("Olist E-Commerce Data Analysis Dashboard")

st.markdown("""
Dashboard ini menyajikan hasil **Exploratory Data Analysis (EDA)** pada dataset Olist,
dengan fokus pada **distribusi pelanggan & revenue per state** serta
**hubungan delivery time dengan review score**.
""")

customers, orders, payments, reviews = load_data()

st.header("Distribusi Pelanggan & Revenue per State")

state_summary = customers_vs_revenue_per_state(customers, orders, payments)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 State berdasarkan Jumlah Pelanggan")
    st.dataframe(state_summary.head(10), use_container_width=True)

with col2:
    st.subheader("Customers vs Revenue")
    fig, ax = plt.subplots()
    ax.scatter(
        state_summary["total_customers"],
        state_summary["total_revenue"] / 1_000_000,
        alpha=0.6
    )
    ax.set_xlabel("Total Customers")
    ax.set_ylabel("Total Revenue (Million)")
    st.pyplot(fig)

st.markdown("""
**Insight:**  
State seperti **Sao Paulo (SP)** memiliki konsentrasi pelanggan dan revenue tertinggi,
menunjukkan dominasi wilayah tersebut dalam aktivitas e-commerce.
""")

st.header("Delivery Time vs Review Score")

delivery_review_df = prepare_delivery_review_df(orders, reviews)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(
        delivery_review_df["delivery_time_days"],
        delivery_review_df["review_score"],
        alpha=0.3
    )
    ax.set_xlabel("Delivery Time (days)")
    ax.set_ylabel("Review Score")
    st.pyplot(fig)

with col4:
    st.subheader("Statistik Korelasi (Spearman)")
    corr = delivery_review_df[["delivery_time_days", "review_score"]].corr(method="spearman")
    st.dataframe(corr)

st.markdown("""
**Insight:**  
Terdapat **korelasi negatif lemah** antara lama waktu pengiriman dan skor ulasan.
Pengiriman yang lebih lama cenderung diikuti skor ulasan yang lebih rendah,
meskipun bukan satu-satunya faktor yang memengaruhi kepuasan pelanggan.
""")

st.markdown("---")
st.caption("Olist E-Commerce Analysis • Streamlit Dashboard")
