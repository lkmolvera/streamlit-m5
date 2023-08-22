import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Actívate - Gráficos')

# Cargar datos
walmart_link = 'walmart.csv'
data = pd.read_csv(walmart_link)

# Primer Gráfico de Barras (Ventas por Categoría)
st.header('Ventas por Categoría')

fig1, ax1 = plt.subplots()
x_pos = data['Category']
y_pos = data['Sales']

ax1.bar(x_pos, y_pos)

st.pyplot(fig1)

st.markdown('_______________')

# Segundo Gráfico Pay (Utilidad por Región)
st.header('Utilidad por Región')

#Crear dataframe agrupado
profit_region = data[['Region', 'Profit']].groupby(['Region']).sum()
profit_region = profit_region.reset_index()

fig2, ax2 = plt.subplots()
labels = profit_region['Region']
profits = profit_region['Profit']

ax2.pie(profits, labels=labels, autopct='%1.1f%%', startangle=90)

st.pyplot(fig2)