import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt 

st.title("Dashboard del MotionLAB")
archivo = st.file_uploader("aca va el archivo", type= "csv") 

if archivo is not None:
    try: 
        df = pd.read_csv(archivo)

 