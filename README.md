# Machine-Learning-Brazilian-E-Commerce
This Repository is used for study case for joining GDGoC UNSRI

## Description

Proyek ini bertujuan untuk melakukan **Analisis Data pada dataset Brazilian E-Commerce (Olist)** guna menemukan insight bisnis terkait **perilaku pelanggan, distribusi pendapatan antar negara bagian, serta hubungan antara waktu pengiriman dan kepuasan pelanggan**.
Selain analisis eksploratif, hasil analisis disajikan melalui **dashboard interaktif menggunakan Streamlit**.

---

## Dataset

Dataset yang digunakan adalah [**Brazilian E-Commerce Public Dataset by Olist**](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), yang mencakup informasi:

* Pelanggan (customers)
* Pesanan (orders)
* Pembayaran (payments)
* Item pesanan (order items)
* Produk dan kategori
* Penjual (sellers)
* Ulasan pelanggan (reviews)
* Informasi lokasi (geolocation)

Dataset berbentuk file CSV dan digunakan untuk keperluan analisis deskriptif dan eksploratif.

---

## Installation

### Setup Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependency

```bash
pip install -r requirements.txt
```

### Menjalankan Dashboard (Streamlit)

```bash
streamlit run app.py
```

---

## Ringkasan Insight Hasil Analisis

### 1. Konsentrasi Pelanggan & Revenue per State

* **Sao Paulo (SP)** memiliki konsentrasi pelanggan tertinggi dan menyumbang **total revenue terbesar**, jauh melampaui negara bagian lain.
* Distribusi revenue sangat **tidak merata**, dengan sebagian besar pendapatan terpusat di negara bagian besar seperti **SP, RJ, dan MG**.
* Beberapa negara bagian dengan jumlah pelanggan rendah justru memiliki **rata-rata revenue per customer yang tinggi**, menunjukkan potensi pasar bernilai tinggi meskipun volumenya kecil.

### 2. Delivery Time vs Review Score

* Terdapat **korelasi negatif lemah** antara lama waktu pengiriman dan skor ulasan pelanggan.
* Semakin lama waktu pengiriman, **cenderung** skor ulasan menurun.
* Pesanan dengan waktu pengiriman **>30 hari** menunjukkan penurunan signifikan pada median skor ulasan.
* Namun, waktu pengiriman **bukan satu-satunya faktor**, karena masih terdapat ulasan tinggi pada beberapa kasus pengiriman lama.

---

## Dashboard

Dashboard Streamlit menampilkan:

* Distribusi pelanggan dan revenue per state
* Visualisasi hubungan delivery time dan review score
* Ringkasan insight utama dalam bentuk visual yang mudah dipahami

Dashboard dirancang untuk dijalankan secara lokal dan dapat dikembangkan lebih lanjut untuk deployment online.

---

## Tools

* Python
* Pandas
* Matplotlib
* Streamlit
* Jupyter Notebook
* Google Colab
