import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load Model Machine Learning
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

def show():
    # Judul Halaman
    st.markdown(
        """
        <h1 style="text-align: center; color: #2F4F4F;">Hasil Prediksi dan Grafik</h1>
        <hr style="border-top: 3px solid #2F4F4F;">
        """, 
        unsafe_allow_html=True
    )
    
    # Ambil data dari session state
    data_input = st.session_state.get("data_input", {})
    nama = st.session_state.get("nama", "Pengguna")
    umur = st.session_state.get("umur", "-")

    if not data_input:
        st.error("Harap isi data di halaman Input Data!")
        return

    # Konversi Data ke DataFrame
    df_input = pd.DataFrame([data_input])

    # Prediksi Risiko Diabetes
    prediksi = model.predict(df_input)[0]
    risiko = "Resiko Diabetes Tinggi" if prediksi == 1 else "Resiko Diabetes Rendah"

    # Menampilkan Informasi Pengguna
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background-color: #F0F8FF; padding: 20px; border-radius: 10px;">
        <h3 style="color: #2E8B57;">Nama: {nama}</h3>
        <p style="font-size: 18px;">Umur: {umur} tahun</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background-color: #FFE4E1; padding: 20px; border-radius: 10px;">
        <h3 style="color: #8B0000;">Prediksi:</h3>
        <h4>{risiko}</h4>
        </div>
        """, unsafe_allow_html=True)

    # Grafik Data Input
    st.markdown("### Grafik Data yang Dimasukkan")
    fig, ax = plt.subplots(figsize=(8, 4))  # Grafik lebih kecil
    sns.barplot(x=df_input.columns, y=df_input.iloc[0].values, palette="muted", ax=ax)
    ax.set_xticklabels(df_input.columns, rotation=45, ha="right")
    ax.set_title("Visualisasi Data Input", fontsize=14, color="#333333")
    ax.set_ylabel("Nilai", fontsize=12)
    ax.set_xlabel("Fitur", fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)

    # Tombol Kembali
    if st.button("Kembali ke Halaman Awal"):
        st.session_state["halaman"] = "Home"  # Pindah ke halaman Home
