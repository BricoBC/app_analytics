import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Brico's Analytics", page_icon="📊", layout="wide")
st.title('Analisis desde la web')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)