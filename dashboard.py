import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Membaca data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Menentukan pertanyaan bisnis
pertanyaan_1 = "Pada hari apa penyewaan sepeda yang paling banyak dan paling sedikit di hari kerja?"
pertanyaan_2 = "Apa pengaruh musim terhadap jumlah sewa sepeda?"

# Sidebar
st.sidebar.title("Analisis Data Bike Sharing")
st.sidebar.markdown("*Pertanyaan Bisnis:*")
st.sidebar.markdown("- " + pertanyaan_1)
st.sidebar.markdown("- " + pertanyaan_2)

# Tab - Pertanyaan 1
tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])

with tab1:
    # Mengambil data hari kerja
    filtered_data_wDay = day_df[day_df["workingday"] == 1]

    # Menampilkan visualisasi
    st.subheader("Jumlah Sewa di Hari Kerja")
    plt.figure(figsize=(8, 6))
    sns.barplot(x="weekday", y="cnt", data=filtered_data_wDay)
    plt.xlabel("Hari Kerja")
    plt.ylabel("Jumlah Sewa Sepeda")
    # Memberikan figur sebagai argumen ke st.pyplot()
    st.pyplot(plt.gcf())

    # Kesimpulan
    st.markdown("*Kesimpulan:*")
    st.markdown(
        "- Puncak sewa terjadi pada hari ke-4, menunjukkan minat pelanggan menggunakan sepeda pada hari tersebut."
    )
    st.markdown(
        "- Jumlah sewa sepeda paling sedikit terjadi pada hari ke-1, menunjukkan minat yang lebih rendah pada awal periode."
    )
    st.markdown(
        "- Pola penggunaan sepeda: Terjadi peningkatan penggunaan sepeda dari hari ke-1 hingga ke-4."
    )

with tab2:
    # Menghitung total sewa untuk setiap musim
    season_counts = day_df.groupby("season").size()

    # Menampilkan visualisasi
    st.subheader("Pengaruh Musim terhadap Jumlah Sewa Sepeda")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=season_counts.index, y=season_counts, ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Sewa Sepeda")
    st.pyplot(fig)
    
    # Kesimpulan
    st.markdown("*Kesimpulan:*")
    st.markdown(
        "- Berdasarkan data yang tersedia, dapat disimpulkan bahwa musim tidak memiliki pengaruh signifikan terhadap jumlah sepeda yang disewa."
    )
    st.markdown(
        "- Pola Penggunaan Sepeda: Stabil: Tidak ada perubahan signifikan dalam jumlah sewa di berbagai musim."
    )
