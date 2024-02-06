import streamlit as st
import pandas as pd
import numpy as np
import datetime

data = None
st.set_page_config(page_title="Brico's Analytics", page_icon="📊", layout="wide")
    
def showCharts(file):
    st.title('Análisis de la Tienda')
    df = pd.read_excel(data)
    

def sidebar():
    with st.sidebar:
        type_file = ['csv', 'excel']
        file = st.radio('Tipo de archivo: ', type_file)
        
        if file == 'excel':
            data = st.file_uploader('Carga el archivo para empezar ', type=["xlsx"])        
        if file == 'csv' :            
            data = st.file_uploader('Carga el archivo para empezar ', type=["csv"], accept_multiple_files=True)        
                        



# year_start = st.sidebar.date_input("Selecciona la fecha de inicio", value = datetime.date(2019, 7, 6), min_value=datetime.date(2019, 1, 1)
#                              , max_value= datetime.date(2021, 12, 31))
# year_end = st.sidebar.date_input("Selecciona la fecha de final", value = datetime.date(2019, 7, 6), min_value=datetime.date(2019, 1, 1)
#                              , max_value= datetime.date(2021, 12, 31))


if data is not None:
    showCharts(data)
    
if __name__ == '__main__':
    sidebar()