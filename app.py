import streamlit as st
import pandas as pd
import numpy as np
import datetime


st.set_page_config(page_title="Brico's Analytics", page_icon="📊", layout="wide")
    
def showCharts(file):
    st.title('Análisis para el '+ str(year))
    df = pd.read_csv(data)
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d-%m-%Y')

    df = df[df['Fecha'].dt.year == year]

    st.write(df.loc[:, ['Productos', 'Ingreso', 'Tienda']])
    
    tiendas = df['Tienda'].unique()
    st.write(tiendas)
    
    
    
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)

# Add a slider to the sidebar:
data = st.sidebar.file_uploader('Carga el archivo para empezar ')
year = st.sidebar.number_input('Insert a number', min_value=2019, max_value=2021, step=1)


# year_start = st.sidebar.date_input("Selecciona la fecha de inicio", value = datetime.date(2019, 7, 6), min_value=datetime.date(2019, 1, 1)
#                              , max_value= datetime.date(2021, 12, 31))
# year_end = st.sidebar.date_input("Selecciona la fecha de final", value = datetime.date(2019, 7, 6), min_value=datetime.date(2019, 1, 1)
#                              , max_value= datetime.date(2021, 12, 31))


if data is not None:
    showCharts(data)