import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de Vehículos en Venta - USA')
car_data = pd.read_csv('data/vehicles_us.csv')

# Botón para histograma
if st.button('Construir histograma'):
    st.write('Histograma de odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para scatter plot
if st.button('Construir diagrama de dispersión'):
    st.write('Diagrama de odómetro vs precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
