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

        # Customizable Plot

        st.subheader("Customizable Plot")
        all_columns_names = df.columns.tolist()
        type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
        selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

        if st.button("Generate Plot"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

            # Plot By Streamlit
            if type_of_plot == 'area':
                cust_data = df[selected_columns_names]
                st.area_chart(cust_data)
                
            elif type_of_plot == 'bar':
                cust_data = df[selected_columns_names]
                st.bar_chart(cust_data)
                
            elif type_of_plot == 'line':
                cust_data = df[selected_columns_names]
                st.line_chart(cust_data)

		    # Custom Plot 

            elif type_of_plot:
                cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
                st.write(cust_plot)
                st.pyplot()