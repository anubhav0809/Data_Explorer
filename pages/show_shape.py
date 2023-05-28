import streamlit as st
import pandas as pd
import os

def app():
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    
    else:
        df = pd.read_csv('data/main_data.csv')

    if st.checkbox("Shape of Dataset"):
        data_dim = st.radio("Show Dimension By ",("Rows","Columns"))
        if data_dim == 'Rows':
            st.text("Number of Rows")
            st.write(df.shape[0])
        elif data_dim == 'Columns':
            st.text("Number of Columns")
            st.write(df.shape[1])
        else:
            st.write(df.shape)