import streamlit as st
import pandas as pd

st.title('Netflix App')

# Ubicación datos
netflix_link = 'movies.csv'
full_movies = pd.read_csv(netflix_link)


# Función para cargar datos
@st.cache
def load_data(rows):
    movies_data = pd.read_csv(netflix_link, nrows=rows)
    return movies_data

def load_movies_title(name):
    filtered_title = full_movies[full_movies['name'].str.upper().str.contains(name)]
    return filtered_title

def load_movies_director(director):
    filtered_director = full_movies[full_movies['director']==director]
    return filtered_director

st.header('Todas las películas')

# Sidebar
sidebar = st.sidebar
sidebar.title("Titulo de barra lateral")
sidebar.write("Informacion de mi sidebar")

# Checkbox
movies = load_data(500)

if sidebar.checkbox('Mostrar todas las películas'):
    st.dataframe(movies)

# Buscar por título
myname = sidebar.text_input('Name :')
btnFilterbyTitle = sidebar.button('Filter by Film')

if(btnFilterbyTitle):
    filterbyname = load_movies_title(myname.upper())
    count_row = filterbyname.shape[0]
    st.write(f'Total Movies: {count_row}')

    st.dataframe(filterbyname)


# Buscar por director
selected_director   = sidebar.selectbox('Select Director', full_movies['director'].unique())
btnFilterbyDirector = sidebar.button('Filter by Director')

if(btnFilterbyDirector):
    filterbydirector = load_movies_director(selected_director)
    count_row = filterbydirector.shape[0]
    st.write(f'Total Movies: {count_row}')

    st.dataframe(filterbydirector)
