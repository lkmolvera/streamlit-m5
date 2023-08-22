import streamlit as st 
import pandas as pd 

st.title('Actívate - Controles Streamlit')
st.header('Slider, Radio, Selectbox')

walmart_link = 'walmart.csv'

# Función para cargar datos
@st.cache
def load_data():
    data = pd.read_csv(walmart_link)
    return data

#Función para filtrar los datos
@st.cache
def load_data_byshipmode_category_discount(shipmode, category, discount):
    data = pd.read_csv(walmart_link)
    filtered_data_byshipmodecategorydiscount = data[ (data['Ship Mode'] == shipmode) & (data['Category'] == category) & (data['Discount'] <= discount)]
    return filtered_data_byshipmodecategorydiscount

# Se cargan los datos
data = load_data()

# Se configuran los controles
selected_shipmode   = st.radio('Select Ship Mode', data['Ship Mode'].unique())
selected_Category   = st.selectbox('Select Category', data['Category'].unique())

optionals = st.expander('Slider Configuration', True)
discount_select = optionals.slider(
    'Select the Discount',
    min_value=float(data['Discount'].min()),
    max_value=float(data['Discount'].max())
)

# Se coloca un botón para presionar cuando se tengan las selecciones listas
btnFilter = st.button('Filter Data')

# Se realizan las selecciones de los controles en los datos utilizando la función para filtrar datos
if (btnFilter):
    filterbyshipmodecategorydiscount = load_data_byshipmode_category_discount( selected_shipmode,  selected_Category, discount_select)
    count_row = filterbyshipmodecategorydiscount.shape[0]
    st.write(f"Total items : {count_row}")

    st.dataframe(filterbyshipmodecategorydiscount)

