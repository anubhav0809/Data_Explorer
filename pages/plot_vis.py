import streamlit as st
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def app():
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    
    else:
        df = pd.read_csv('data/main_data.csv')

        # Plot and Visualization

        st.subheader("Data Visualization")
        # Correlation
	    # Seaborn Plot
        if st.checkbox("Correlation Plot[Seaborn]"):
            st.write(sns.heatmap(df.corr(),annot=True))
            st.pyplot()
        
        # Pie Chart
        if st.checkbox("Pie Plot"):
            all_columns_names = df.columns.tolist()
            if st.button("Generate Pie Plot"):
                st.success("Generating A Pie Plot")
                st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
                st.pyplot()

        # Count Plot
        if st.checkbox("Plot of Value Counts"):
            st.text("Value Counts By Target")
            all_columns_names = df.columns.tolist()
            primary_col = st.selectbox("Primary Columm to GroupBy",all_columns_names)
            selected_columns_names = st.multiselect("Select Columns",all_columns_names)
            if st.button("Plot"):
                st.text("Generate Plot")
                if selected_columns_names:
                    vc_plot = df.groupby(primary_col)[selected_columns_names].count()
                else:
                    vc_plot = df.iloc[:,-1].value_counts()
                st.write(vc_plot.plot(kind="bar"))
                st.pyplot()

