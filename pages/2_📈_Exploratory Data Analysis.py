# Import necessary packages
import pandas as pd
import numpy as np
import streamlit as st
from utils import barplot, boxplot, outliers, scatterplot

# Config other things in the page
st.set_option('deprecation.showPyplotGlobalUse', False)
df = pd.read_csv('listings.csv.gz')

# Set page config
st.set_page_config(
    page_title="Airbnb EDA",
    page_icon="📈"
)

# 1. Title the app
st.title('Exploratory Data Analysis for Airbnb in Rio de Janeiro 📈')
st.markdown('**Lets get some information, insights and curiosities about Airbnb in Rio de Janeiro? Lets go!** :sun_with_face: :eyeglasses:')

# 2. Barplot - neighbourhood
df_filtered = df.groupby(by=["neighbourhood_cleansed"], dropna=True).agg({'neighbourhood_cleansed' : ['count']}).reset_index()
df_filtered = df_filtered.sort_values(('neighbourhood_cleansed', 'count'), ascending=False).head(10)
df_filtered.columns = ['neighbourhood_cleansed', 'count']
lst = df_filtered.neighbourhood_cleansed.unique().tolist()
df_filtered.neighbourhood_cleansed.replace({'Recreio dos Bandeirantes': 'Recreio'}, inplace=True)

st.pyplot(barplot.barplot((15, 5), 'The ten neighborhoods with the most properties on Rio Airbnb', df_filtered,
                          'neighbourhood_cleansed', 'count', 'Neighbourhood', 'Count'))
st.markdown('Copacabana neighbourhood has more Airbnb locations than any other. **Copacabana has almost 14x more Airbnb:scream_cat: than the last one on the list and almost 3x more than the second and third place, Ipanema and Barra da Tijuca, respectively.**')

# 3. Barplot - roomtype
df_filtered2 = df.groupby(by=["room_type"]).count().reset_index().sort_values('id', ascending=False)

st.pyplot(barplot.barplot((15, 5), 'The distribuition of room types on Rio Airbnb', df_filtered2,
                          df_filtered2.room_type, df_filtered2.id, 'Room Type', 'Count'))
st.markdown('In Rio de Janeiro, you will find many more houses and apartments for rent. **There are almost 4x more offers than the second place, "private room".** :house: :chart_with_upwards_trend:')

# 4. Boxplot - price distribuition of the neighbourhood with the most properties
df.price = df.price.str.replace('$', '').str.replace(',', '').astype(float)
df_filtered3 = df.loc[(df['neighbourhood_cleansed'] == lst[0]) |
                      (df['neighbourhood_cleansed'] == lst[1]) |
                      (df['neighbourhood_cleansed'] == lst[2]) |
                      (df['neighbourhood_cleansed'] == lst[3]) |
                      (df['neighbourhood_cleansed'] == lst[4]) |
                      (df['neighbourhood_cleansed'] == lst[5]) |
                      (df['neighbourhood_cleansed'] == lst[6]) |
                      (df['neighbourhood_cleansed'] == lst[7]) |
                      (df['neighbourhood_cleansed'] == lst[8])]
df_filtered3.neighbourhood_cleansed.replace({'Recreio dos Bandeirantes': 'Recreio'}, inplace=True)
numerical_cols = ['accommodates', 'bathrooms', 'bedrooms', 'beds', 'price']
for col in numerical_cols:
    outliers.exclui_outliers(df_filtered3, col)

st.pyplot(boxplot.boxplot((15, 5), 'The distribuition of price in the neighborhoods with the most properties', df_filtered3,
                          'neighbourhood_cleansed', 'price', 'Neighbourhood', 'Price Distribuition'))

st.caption('Statistical summary of prices by neighborhood')
st.table(df_filtered3.groupby(by=["neighbourhood_cleansed"]).agg({'price' : ['min', 'max', 'mean', 'median', np.std]}))
st.markdown('Well, it seems that Copacabana lost the first place:stuck_out_tongue_winking_eye:, see that the median price is only 258.00 reals, much lower than Barra, Ipanema, Leblon and Recreio, which are already in the range of 400.00 reals:money_with_wings:. **Note that it is preferable to look at the median in this case, as we have a lot of extreme values in this dataset.**')
st.empty()
st.markdown('**If you want a cheaper place, bet on the downtown and Santa Teresa regions.**	:money_mouth_face:')

# 5. Boxplot - Availability of the neighbourhood with the most properties
st.pyplot(boxplot.boxplot((15, 5), 'The distribuition of availability in the neighborhoods with the most properties', df_filtered3,
                          'neighbourhood_cleansed', 'availability_365', 'Neighbourhood', 'Availability Distribuition'))
st.markdown('It seems that all these neighborhoods that we are studying have good availability throughout the year. Good for travelers!:small_airplane:')

# 6. scatterplot - prices per neighbourghood
outliers.exclui_outliers(df, col)
st.pyplot(scatterplot.scatter((10, 6), 'Map of Price Distribution in all neighbourhoods', df,
                              'latitude', 'longitude', 'price', 'Latitude', 'Longitude'))
st.markdown('Not much information or pattern here, just a mess!')

# 7. statistical summary - reviews
st.caption('Statistical summary of reviews by neighborhood')
st.table(df_filtered3.groupby(by=["neighbourhood_cleansed"]).agg({'review_scores_value' : ['mean', 'median', np.std]}))
st.markdown('Looks like travelers are going to be happy again, the mean and median review scores are pretty high! And all this with a relatively low standard deviation. Wonderful!	:smile:')
st.empty()
st.markdown('Well, lets end the story here.:wave:')