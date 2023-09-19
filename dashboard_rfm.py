import streamlit as st
import pandas as pd

# Load data hasil RFM analysis
rfm_df = pd.read_csv("hasil_rfm.csv")

# Judul dashboard
st.title('Dashboard RFM Analysis')

# Tampilkan hasil RFM analysis
st.write('Hasil RFM Analysis:')
st.write(rfm_df)

# Tambahkan visualisasi atau grafik sesuai kebutuhan
# Misalnya, Anda dapat menambahkan grafik histogram untuk Frequency atau Monetary

# Tampilkan grafik histogram untuk Frequency
st.write('Histogram Frequency:')
st.bar_chart(rfm_df['frequency'])

# Tampilkan grafik histogram untuk Monetary
st.write('Histogram Monetary:')
st.bar_chart(rfm_df['monetary'])