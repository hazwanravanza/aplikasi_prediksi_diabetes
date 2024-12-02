import streamlit as st

def show():
    st.markdown(
        """
        <h1 style="text-align: center; color: #4682B4;">Aplikasi Prediksi Risiko Diabetes</h1>
        <p style="text-align: center; color: #555555; font-size: 18px;">
        Aplikasi ini membantu memprediksi risiko diabetes berdasarkan data kesehatan dan gaya hidup Anda.
        </p>
        <hr style="border-top: 3px solid #4682B4;">
        """, 
        unsafe_allow_html=True
    )

    # Input Nama dan Umur
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama", placeholder="Masukkan nama Anda")
    with col2:
        umur = st.number_input("Umur", min_value=18, max_value=100, step=1, format="%d")
    
    # Tombol untuk Lanjutkan
    if st.button("Lanjutkan ke Input Data"):
        if nama and umur:
            st.session_state["nama"] = nama
            st.session_state["umur"] = umur
            st.session_state["halaman"] = "Input Data"  # Pindah ke halaman Input Data
        else:
            st.error("Harap isi nama dan umur!")
