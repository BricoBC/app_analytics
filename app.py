import streamlit as st
import pandas as pd
import numpy as np
import datetime
import re

st.set_page_config(page_title="Brico's Analytics", page_icon="📊", layout="wide")

# def useExcel(df):
#     file = pd.ExcelFile(file)
#     sheet_names = file.sheet_names        
#     for i in range(len(sheet_names)):        
#         df.append(pd.read_excel(file, sheet_name=sheet_names[i]))            
#         st.write(df[i])
        
# def useCSV(files, table_find_representants):
#     df = []
#     for i in range(len(files)):
#         df.append( pd.read_csv(files[i]) )
#         st.write(df[i])
    
#     arrAllRepresentants = df[table_find_representants]['Representante'].unique()    
    
#     options = st.multiselect('Elige el/la/los representantes: ', 
#                              arrAllRepresentants)
#     st.write('You selected:', options)
    
#     if len(options) > 0 :
#         for i in range(len(options)):
#             st.write( df[table_find_representants][ df[table_find_representants]['Representante'] == options[i] ])
            
        
        
        
    
def file_to_df(file, type_file ):    
    df = []
    st.title('Análisis de la Tienda')
    st.title(type_file)
    
    if type_file == 'excel':        
        file = pd.ExcelFile(file)
        sheet_names = file.sheet_names        
        for i in range(len(sheet_names)):        
            df.append(pd.read_excel(file, sheet_name=sheet_names[i]))            
        return df      
        
    if type_file == 'csv':
        df = []
        for i in range(len(file)):
            df.append( pd.read_csv(file[i]) )            
        return df

def sidebar():
    data = None or []
    showInfo = False    
    with st.sidebar:
        type_file = ['csv', 'excel']
        type_file = st.radio('Tipo de archivo: ', type_file, index=None)
        
        if type_file == 'excel':
            data = st.file_uploader('Carga el archivo para empezar ', type=["xlsx"])                       
            if data is not None:
                showInfo =  True
            
        if type_file == 'csv' :            
            data = st.file_uploader('Carga el archivo para empezar ', type=["csv"], accept_multiple_files=True)                          
            if len(data) > 0:
                showInfo =  True
                
                    
            
    if showInfo:
        df = file_to_df(data, type_file)                
        st.write(df)
        
    
if __name__ == '__main__':    
    sidebar()