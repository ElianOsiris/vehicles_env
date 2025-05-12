import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la aplicación
st.header('Exploración de Datos de Vehículos Usados')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar los primeros registros
st.subheader('Vista previa de los datos')
st.write(car_data.head(100))

# Casilla de verificación para construir histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para construir gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión (odómetro vs precio)')

if build_scatter:
    st.write('Creación de un gráfico de dispersión: precio vs odómetro')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre el kilometraje y el precio")
    st.plotly_chart(fig_scatter, use_container_width=True)

build_pattern_shape = st.checkbox('Mostrar gráfico de patrón de forma')

if build_pattern_shape:
    st.write('Creación de un gráfico de patrón de forma: precio por tipo de combustible y modelo')
    # Crear gráfico de patrón de forma
    fig = px.treemap(car_data, path=['fuel', 'model'], values='price')
    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación
build_pattern_shape = st.checkbox('Construir gráfico con patrón de forma')

if build_pattern_shape:
    st.header('Gráfico con textura (pattern shape)')
    st.write('Creación de un gráfico de patrón de forma: precio promedio por tipo de combustible')

    # Agrupar datos por combustible y obtener precio promedio
    grouped_data = car_data.groupby('fuel', as_index=False)['price'].mean()

    # Crear gráfico de barras con patrones
    fig = px.bar(
        grouped_data,
        x='fuel',
        y='price',
        pattern_shape='fuel',  # patrón por categoría
        title='Precio promedio por tipo de combustible',
        labels={'price': 'Precio promedio', 'fuel': 'Tipo de combustible'}
    )

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)