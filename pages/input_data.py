import streamlit as st

def konversi_input(tekanan_darah, kolesterol, bmi, perokok, stroke, penyakit_jantung,
                   aktivitas_fisik, alkohol, nodoc, kesehatan_umum, kesehatan_mental,
                   kesehatan_fisik, kesulitan_berjalan, pendidikan, pendapatan, umur_kelompok):
    return {
        "HighBP": 1 if tekanan_darah == "Ya" else 0,
        "HighChol": 1 if kolesterol == "Ya" else 0,
        "BMI": bmi,
        "Smoker": 1 if perokok == "Ya" else 0,
        "Stroke": 1 if stroke == "Ya" else 0,
        "HeartDiseaseorAttack": 1 if penyakit_jantung == "Ya" else 0,
        "PhysActivity": 1 if aktivitas_fisik == "Ya" else 0,
        "HvyAlcoholConsump": 1 if alkohol == "Ya" else 0,
        "NoDocbcCost": 1 if nodoc == "Ya" else 0,
        "GenHlth": kesehatan_umum,
        "MentHlth": kesehatan_mental,
        "PhysHlth": kesehatan_fisik,
        "DiffWalk": 1 if kesulitan_berjalan == "Ya" else 0,
        "Education": ["Tidak Pernah Sekolah", "Sekolah Dasar", "SMP", "SMA", "Sarjana", "Magister"].index(pendidikan) + 1,
        "Income": ["Kurang dari $10,000", "Kurang dari $35,000", "$75,000 atau lebih"].index(pendapatan) + 1,
        "Age": ["18-24", "25-29", "30-34", "35-39", "40-44", "45-49", 
                "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80+"].index(umur_kelompok) + 1
    }

def show():
    st.markdown(
        """
        <h1 style="text-align: center; color: #4682B4;">Input Data Pengguna</h1>
        <p style="text-align: center; color: #555555;">Isi semua data di bawah ini dengan benar untuk memproses prediksi.</p>
        <hr style="border-top: 3px solid #4682B4;">
        """, 
        unsafe_allow_html=True
    )

    # Input data
    tekanan_darah = st.selectbox("Tekanan Darah Tinggi", ["Tidak", "Ya"])
    kolesterol = st.selectbox("Tinggi Kolesterol", ["Tidak", "Ya"])
    bmi = st.number_input("Body Mass Index (BMI)", min_value=10, max_value=50, step=1)
    perokok = st.selectbox("Apakah Anda Merokok?", ["Tidak", "Ya"])
    stroke = st.selectbox("Apakah Anda Pernah Stroke?", ["Tidak", "Ya"])
    penyakit_jantung = st.selectbox("Penyakit Jantung Coroner", ["Tidak", "Ya"])
    aktivitas_fisik = st.selectbox("Aktivitas Fisik Bulan Ini", ["Tidak", "Ya"])
    alkohol = st.selectbox("Apakah Anda Mengonsumsi Alkohol?", ["Tidak", "Ya"])
    nodoc = st.selectbox("Tidak ke Dokter karena Biaya?", ["Tidak", "Ya"])
    kesehatan_umum = st.slider("Penilaian Kesehatan Umum", 1, 5)
    kesehatan_mental = st.slider("Kesehatan Mental (0-30 hari)", 0, 30, 1)
    kesehatan_fisik = st.slider("Kesehatan Fisik (0-30 hari)", 0, 30, 1)
    kesulitan_berjalan = st.selectbox("Kesulitan Berjalan/Menaiki Tangga", ["Tidak", "Ya"])
    pendidikan = st.selectbox("Pendidikan Terakhir", ["Tidak Pernah Sekolah", "Sekolah Dasar", "SMP", "SMA", "Sarjana", "Magister"])
    pendapatan = st.selectbox("Pendapatan Tahunan", ["Kurang dari $10,000", "Kurang dari $35,000", "$75,000 atau lebih"])
    umur_kelompok = st.selectbox("Kelompok Umur", ["18-24", "25-29", "30-34", "35-39", "40-44", 
                                                    "45-49", "50-54", "55-59", "60-64", "65-69", 
                                                    "70-74", "75-79", "80+"])

    if st.button("Simpan Data dan Lanjutkan"):
        data_konversi = konversi_input(
            tekanan_darah, kolesterol, bmi, perokok, stroke, penyakit_jantung,
            aktivitas_fisik, alkohol, nodoc, kesehatan_umum, kesehatan_mental,
            kesehatan_fisik, kesulitan_berjalan, pendidikan, pendapatan, umur_kelompok
        )
        st.session_state["data_input"] = data_konversi
        st.session_state["halaman"] = "Hasil dan Grafik"  # Pindah ke halaman Hasil dan Grafik
        st.success("Data berhasil disimpan! Silakan ke halaman hasil prediksi.")
