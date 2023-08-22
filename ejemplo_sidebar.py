import streamlit as st 

# crear title de la app web
st.title("Mi primera app con Streamlit")
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral.")
sidebar.write("Aquí van los elementos de entrada.")

st.header("Información sobre el Conjunto de Datos")

st.header("Descripción de los datos")

st.write("""

Este es un simple ejemplo de una app para predecir. 

Esta app predice mis datos!
""")

