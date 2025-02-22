import streamlit as st
import pandas as pd
import numpy as np

def app():
    nilai = []
    k1_arr = []
    k2_arr = []
    k3_arr = []
    k4_arr = []
    k5_arr = []
    k1_norm = []
    k2_norm = []
    k3_norm = []
    k4_norm = []
    k5_norm = []
    res = []
    hasil = []

    st.title("SISTEM PENDUKUNG KEPUTUSAN PENILAIAN KINERJA DOSEN")
    dosen = ["DOSEN-01","DOSEN-02","DOSEN-03","DOSEN-04","DOSEN-05","DOSEN-06","DOSEN-07",]

    for i in dosen:
        st.title(i)
        k1 = st.radio("1. Penguasaan dan kemampuan dalam menjelaskan",(1,2,3,4,5),key=i+"k1",horizontal=True)
        nilai.append(k1)
        k1_arr.append(k1)

        k2 = st.radio("2. Kemampuan dalam menjawab pertanyaan",(1,2,3,4,5),key=i+"k2",horizontal=True)
        nilai.append(k2)
        k2_arr.append(k2)

        k3 = st.radio("3. Kemampuan dalam memberi motivasi mahasiswa",(1,2,3,4,5),key=i+"k3",horizontal=True)
        nilai.append(k3)
        k3_arr.append(k3)

        k4 = st.radio("4. Kemampuan membuat suasana kelas menyenangkan",(1,2,3,4,5),key=i+"k4",horizontal=  True)
        nilai.append(k4)
        k4_arr.append(k4)

        k5 = st.radio("5. Kedisiplinan hadir dalam perkuliahan",(1,2,3,4,5),key=i+"k5",horizontal=True)
        nilai.append(k5)
        k5_arr.append(k5)
      
    st.title("Data Dosen")
    df = pd.DataFrame({"Dosen":dosen, "K1": k1_arr, "K2": k2_arr, "K3": k3_arr, "K4": k4_arr, "K5": k5_arr})
    st.write(df)

    k1_min = min(k1_arr)
    k1_max = max(k1_arr)

    k2_min = min(k2_arr)
    k2_max = max(k2_arr)

    k3_min = min(k3_arr)
    k3_max = max(k3_arr)

    k4_min = min(k4_arr)
    k4_max = max(k4_arr)

    k5_min = min(k5_arr)
    k5_max = max(k5_arr)

    for i in k1_arr:
        k1_norm.append((i-k1_min)/(k1_max-k1_min))
    
    for i in k2_arr:
        k2_norm.append((i-k2_min)/(k2_max-k2_min))

    for i in k3_arr:
        k3_norm.append((i-k3_min)/(k3_max-k3_min))

    for i in k4_arr:
        k4_norm.append((i-k4_min)/(k4_max-k4_min))

    for i in k5_arr:
        k5_norm.append((i-k5_min)/(k5_max-k5_min))
    
    st.title("Normalisasi Matriks")
    df_norm = pd.DataFrame({"Dosen":dosen,"K1": k1_norm, "K2": k2_norm, "K3": k3_norm, "K4": k4_norm, "K5": k5_norm})
    st.write(df_norm)

    for i in range(7):
        sum = (0.30*k1_norm[i])+(0.15*k2_norm[i])+(0.15*k3_norm[i])+(0.20*k4_norm[i])+(0.20*k5_norm[i])
        res.append(sum)
        if (sum >= 0.60): hasil.append("Kinerja Baik")
        else : hasil.append("Kinerja Buruk")
    ranks = np.array(res).argsort()[::-1].argsort()
    st.title("Hasil")
    st.write("Hasil dari penelitian ini berupa keputusan dosen yang memiliki kinerja baik dan dosen memiliki kinerja buruk, dimana nilai ≥ 0,60 memiliki predikat kinerja baik dan < 60 memiliki kinerja buruk, dan dilakukan juga peringkat berdasarkan nilai preferensi dari setiap dosen.")
    pref = pd.DataFrame({"Dosen":dosen,"Preferensi":res,"Hasil":hasil, "Peringkat": ranks+1})
    st.write(pref)
    