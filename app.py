import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
data = pd.read_csv('resultados_modelo_ventas.csv')

# Título de la app
st.title('Análisis de Ventas')

# Filtro interactivo para seleccionar la categoría de producto
categoria = st.selectbox('Selecciona la categoría de producto:', ['Todas'] + list(data['Categoría_Producto'].unique()))

# Filtrar los datos según la categoría seleccionada
if categoria == 'Todas':
    df_filtrado = data
else:
    df_filtrado = data[data['Categoría_Producto'] == categoria]

# Gráfico de dispersión
st.subheader('Gráfico de Dispersión: Relación entre Precio y Ventas Predichas')
fig_dispersion = px.scatter(df_filtrado, x="Precio", y="Ventas_Predichas",
                            color="Categoría_Producto", title="Relación entre Precio y Ventas Predichas")
st.plotly_chart(fig_dispersion)

# Gráfico de barras
st.subheader('Gráfico de Barras: Ventas Predichas por Categoría de Producto')
fig_barras = px.bar(df_filtrado.groupby('Categoría_Producto')['Ventas_Predichas'].sum().reset_index(),
                    x="Categoría_Producto", y="Ventas_Predichas",
                    color='Categoría_Producto',
                    title="Ventas Predichas por Categoría de Producto")
st.plotly_chart(fig_barras)

# Gráfico de línea
st.subheader('Gráfico de Línea: Ventas Predichas por Mes')
fig_linea = px.line(df_filtrado.groupby('Mes')['Ventas_Predichas'].sum().reset_index(),
                    x="Mes", y="Ventas_Predichas",
                    title="Ventas Predichas por Mes")
st.plotly_chart(fig_linea)
