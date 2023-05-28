import streamlit as st
import pandas as pd
import os

def app():
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    
    else:
        df = pd.read_csv('data/main_data.csv')

        # Select Columns
        if st.checkbox("Select Columns To Show"):
            all_columns = df.columns.tolist()
            selected_columns = st.multiselect("Select",all_columns)
            new_df = df[selected_columns]
            st.dataframe(new_df)

        # Show Values
        if st.checkbox("Value Counts"):
            st.text("Value Counts By Target/Class")
            st.write(df.iloc[:,-1].value_counts())

        # Show Datatypes
        if st.checkbox("Data Types"):
            st.write(df.dtypes)

        # Show Summary
        if st.checkbox("Summary"):
            st.write(df.describe().T)