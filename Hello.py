import streamlit as st
from PIL import Image

# set initial page configs
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# set side bar
def load_about():
	st.sidebar.title("About")
	st.sidebar.info(
		"""
		Doubts or suggestions, please contact:\n📩 vitorbeltrao300@gmail.com
		"""
    )

# Set title and balloons
st.write("# Welcome to Airbnb Analysis 👋")
st.balloons()

# Set airbnb and streamlit images
col1, col2 = st.columns(2)
with col1:
    airbnb_logo = Image.open('assets/airbnb.png')
    st.image(airbnb_logo, width=250)

#with col2:
    st_logo = Image.open('assets/streamlit.jpg')
    st.image(st_logo, width=500)

# Set middle text
st.markdown(
    """
    The app was built from Airbnb's public dataset. The idea was to develop a product that can be used by the company or 
    by customers who want to price their buildings and get information/insights from the data. The following pages 
    indicate:
    - Machine Learning: Automate building prices
    - Exploratory Data Analysis: Bring information and insights
"""
)
st.write("#### 👈 Select a page on the left to view!")

# Load sidebar
load_about()