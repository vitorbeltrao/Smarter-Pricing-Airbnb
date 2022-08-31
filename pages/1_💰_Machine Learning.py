# Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import joblib
import streamlit as st
from utils import outliers
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import preprocessing

# Import saved model
model = joblib.load('elastic_net.pkl')

# Set page config
st.set_page_config(
    page_title="Airbnb Smart Pricing",
    page_icon=":moneybag:"
)

def main():
  # Title the app
  st.title('Smarter pricing for Airbnb in Rio de Janeiro :moneybag:')

  st.markdown("""
   * Use the menu at left to enter with your own parameters
   * Your prediction will appear below
  """)
#################################################################################
  # Config sidebar
  st.sidebar.markdown("## Select the parameters of the property you want to rent")

  latitude = st.sidebar.number_input('Insert the latitude of building')
  longitude = st.sidebar.number_input('Insert the longitude of building')

  accommodates = st.sidebar.slider("Select the number of accommodations:", 1, 10, 5)
  bathrooms = st.sidebar.slider("Select the number of bathrooms:", 1, 10, 3)
  bedrooms = st.sidebar.slider("Select the number of bedrooms:", 1, 10, 4)
  beds = st.sidebar.slider("Select the number of beds:", 1, 10, 4)
  availability_365 = st.sidebar.slider("Select the number days that are available:", 1, 365, 180)

  room_type_Hotel = st.sidebar.selectbox('Is it a hotel room? Select 1 for yes or 0 for no:',
                                         [1, 0])
  room_type_Private = st.sidebar.selectbox('Is it a private room? Select 1 for yes or 0 for no:',
                                           [1, 0])
  room_type_Shared = st.sidebar.selectbox('Is it a shared room? Select 1 for yes or 0 for no:',
                                          [1, 0])
###################################################################################################
  # Config predictions
  inputs = pd.DataFrame(np.array([[latitude, longitude, accommodates, bathrooms, bedrooms,
             beds, room_type_Hotel, room_type_Private, room_type_Shared,
             availability_365]]), columns=['latitude', 'longitude', 'accommodates', 'bathrooms',
              'bedrooms', 'beds', 'room_type_Hotel room', 'room_type_Private room', 'room_type_Shared room',
              'availability_365'])  # our inputs

  if st.button('Predict'):  # making and printing our prediction
      result = model.predict(inputs)

      if result <= 409.00 and result > 0.00:
          updated_res = result.flatten().astype(float)
          st.success('Your Airbnb daily price is: {}'.format(updated_res))

      if result > 409.00:
          st.success('Your Airbnb daily price is: 409.00')

      if result < 0.00:
          st.success('Your Airbnb daily price is: 34.00')
####################################################################################

if __name__ == '__main__':
    main()  # calling the main method