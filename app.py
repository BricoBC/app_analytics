import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Brico's Analytics", page_icon="📊", layout="wide")
st.title('Analisis desde la web')

# Add a slider to the sidebar:
data = st.sidebar.file_uploader('Carga el archivo para empezar: ')

if data is not None:
    df = pd.read_csv(data)
    st.write(df)