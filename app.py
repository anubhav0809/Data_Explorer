import os
import streamlit as st
import numpy as np
from PIL import Image

from multipage import MultiPage
from pages import data_upload, show_shape, data_stats, plot_vis, cust_plot # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("ML Dataset Explorer")
display = Image.open('Logo.jpg')
display = np.array(display)
col1, col2 = st.columns(2)
col1.image(display, width = 300)

# Add all your application here
app.add_page("Upload Data", data_upload.app)
app.add_page("Show Shape", show_shape.app)
app.add_page("Data Analysis", data_stats.app)
app.add_page("Plot and Visualization",plot_vis.app)
app.add_page("Customizable Plot",cust_plot.app)

# The main app
app.run()

