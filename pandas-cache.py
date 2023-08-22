# import streamlit and pandas
import streamlit as st 
import pandas as pd 

#print title
st.title('Streamlit con cache')
DATA_URL = 'dataset.csv'

#set dataset url
@st.cache
def load_data(nrows):
    # create dataframe data, con n rows
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# print text 
data_load_state = st.text('Loading data...')
# call function load data
data = load_data(1000)
# print text done..
data_load_state.text("Done !")

# print dataframe
st.dataframe(data)