import pandas as pd
import numpy as np
import streamlit as st

st.title('Uber pickups in NYC')

DATE_COLUMN = 'Date/Time'
DATA_URL = 'uber-raw-data-sep14_v1.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    #lowercase = lambda x: str(x).lower()
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    #data.rename(lowercase, axis='columns', inplace=True)
    return data

#Se crea el mapa con el slider
data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Done! (using st.cache)')

data=load_data(1000)
st.dataframe(data)

hour_to_filter = st.slider('hour', 0,23,17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#filtered_data = data[data[DATE_COLUMN].dt.round('H').dt.hour]

st.header(hour_to_filter)
st.dataframe(filtered_data)
#df["hour_integer"] = df["datetime"].dt.round("H").dt.hour


st.subheader('Map of all pickups at %s:00' %hour_to_filter)
st.map(filtered_data)

#=====================================================================
#Con estas instrucciones se crea el mapa pero sin el slider
#data = load_data(1000) 
#st.dataframe(data)

#st.map(data)
