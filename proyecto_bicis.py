import streamlit as st
import pandas as pd

st.title('Cycle Rides in NYC')

# Ubicación datos
rides_link = 'citibike-tripdata.csv'
full_rides = pd.read_csv(rides_link)

# Función para cargar datos
@st.cache
def load_data(rows):
    rides_data = pd.read_csv(rides_link, nrows=rows)
    return rides_data

rides = load_data(500)

# Sidebar
sidebar = st.sidebar

if sidebar.checkbox('Show raw data'):
    st.dataframe(rides)


