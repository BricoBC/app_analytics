import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import re

st.set_page_config(page_title="Brico's Analytics", page_icon="📊", layout="wide")

def make_barh_chart(x_values, categories, txt_xlabel):    
    bar_colors = list(plt.cm.tab20.colors)
    fig, ax = plt.subplots()    
    hbar = ax.barh(x_values, categories, color=bar_colors) 
    ax.set_xlabel(txt_xlabel, color='w')         
    ax.bar_label(hbar, fmt='%.0f', padding=-18)        
    plt.gca().tick_params(axis='x', colors='w')  # Color rojo para los ejes x
    
    for i, tick in enumerate(ax.get_yticklabels()):
        tick.set_color(bar_colors[i])  #Color igual al de su barra

    plt.gca().set_facecolor('none')  # Fondo transparente
    plt.gcf().set_facecolor('none')  # Fondo transparente

    return fig

def go_tab_product(df, i_table_representant, i_table_sale, i_table_profit):
    arr_all_products = df[i_table_profit]['Descripción'].unique()
    options = st.multiselect('Elige el prodcuto: ', 
                             arr_all_products)
    
def get_name_products(df,arr_ids_products, i_table_profit):
    arr_product = []    
    for i in range(len(arr_ids_products)):
        name_product = (df[i_table_profit]['Descripción'][ df[i_table_profit]['CódigoProducto'] == arr_ids_products[i]]).to_numpy()                
        arr_product.append( name_product[0] )
    
    return arr_product    
    
def go_tab_representant(df, i_table_representant, i_table_sale, i_table_profit):    
    arr_all_representants = df[i_table_representant]['Representante'].unique()
    
    option_selected_representant = st.selectbox('Lista de los representantes registrados: ', 
                             arr_all_representants, index= None, placeholder='Elige a un representante')   
        
    df_show = None
    
    if option_selected_representant != None:        
        col_left, col_rigth = st.columns([3, 1])
        df_show = df[i_table_sale][ df[i_table_sale]['Representante'] == option_selected_representant ]
        total_sales = df[i_table_sale]['Unidades'].sum()
        with col_left:
            products_sales = df_show.groupby(["Producto"])['Unidades'].sum().reset_index().sort_values(by='Unidades', ascending=False)
            graph = make_barh_chart(products_sales['Producto'].values, products_sales['Unidades'].values, 'Unidades vendidas')
            st.pyplot( graph )
                        
        with col_rigth:         
            representant_total_sales = df_show['Unidades'].sum()
            size = [total_sales, representant_total_sales]            
            labels = ['Otras ventas', option_selected_representant]
            
            st.write(f'Vendió un total de {representant_total_sales} unidades')
            st.write(f'Ganancias: ')
            st.write(f'Ventas totales {total_sales:,}')
        
        
    else:                    
            df_show = df[i_table_sale].sample(n=10)
            st.dataframe( df_show, use_container_width=True )            
    
    
def file_to_df(file, type_file ):    
    print('Cargando archivos')
    df = []
    st.title('Análisis de la Tienda')    
    
    if type_file == 'excel':        
        file = pd.ExcelFile(file)
        sheet_names = file.sheet_names        
        for i in range(len(sheet_names)):        
            df.append( pd.read_excel(file, sheet_name=sheet_names[i]) ) 
        return df      
        
    if type_file == 'csv':
        df = []
        for i in range(len(file)):
            df.append( pd.read_csv(file[i]) )            
        
        return df

def sidebar():
    print('Cargando sidebar')    
    df = None
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
                
                    
            
    i_table_representant, i_table_sale, i_table_profit = -1,-1,-1
    if showInfo:
        df = file_to_df(data, type_file)                
        st.write(df)
        for i in range(len(df)):
            if len(df[i].columns) == 3 :
                i_table_representant = i
            
            if len(df[i].columns) == 4 :
                i_table_sale = i
            
            if len(df[i].columns) == 6 :
                i_table_profit = i
        
        
        df[i_table_sale]['Producto'] =  get_name_products(df, df[i_table_sale]['CódigoProducto'].to_numpy() , i_table_profit)    
        df[i_table_sale] = df[i_table_sale][['Fecha', 'Representante', 'Producto', 'Unidades']]
    
        tab_representant, tab_product, = st.tabs(["Representante", "Producto"])
        with tab_representant:
            go_tab_representant(df, i_table_representant, i_table_sale, i_table_profit)
        
        with tab_product:
            go_tab_product(df, i_table_representant, i_table_sale, i_table_profit)
        
    
if __name__ == '__main__':    
    print('...')
    sidebar()