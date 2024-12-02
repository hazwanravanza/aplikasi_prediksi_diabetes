import streamlit as st
from pages import halaman_awal, input_data, hasil_analisis

# Konfigurasi Aplikasi
st.set_page_config(page_title="Prediksi Diabetes", layout="wide")

# Fungsi untuk menentukan halaman yang sedang aktif
def tampilkan_halaman():
    if st.session_state.get("halaman") == "Input Data":
        input_data.show()
    elif st.session_state.get("halaman") == "Hasil dan Grafik":
        hasil_analisis.show()
    else:
        halaman_awal.show()

# Inisialisasi nilai awal
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "Home"

# Menampilkan halaman aktif
tampilkan_halaman()
