import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="Brico's Analytics", page_icon="📊", layout="wide")
    
def showCharts(file):    
    st.title('Análisis de la Tienda')
    
    

def sidebar():
    data = None or []
    showInfo = False
    with st.sidebar:
        type_file = ['csv', 'excel']
        file = st.radio('Tipo de archivo: ', type_file, index=None)
        
        if file == 'excel':
            data = st.file_uploader('Carga el archivo para empezar ', type=["xlsx"])                    
            if data is not None:
                showInfo =  True
            
        if file == 'csv' :            
            data = st.file_uploader('Carga el archivo para empezar ', type=["csv"], accept_multiple_files=True)              
            if len(data) > 0:
                showInfo =  True
            
    if showInfo:
        showCharts(data)                
    
if __name__ == '__main__':    
    sidebar()