import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
data = pd.read_csv('resultados_modelo_ventas.csv')

# Selección de categoría
categoria = st.selectbox('Selecciona la categoría de producto:', ['Todas'] + list(data['Categoría_Producto'].unique()))

# Filtrar los datos según la categoría seleccionada
if categoria == 'Todas':
    df_filtrado = data
else:
    df_filtrado = data[data['Categoría_Producto'] == categoria]

# Crear gráfico de dispersión
fig_dispersion = px.scatter(df_filtrado, x="Precio", y="Ventas_Predichas", color="Categoría_Producto", title="Relación entre Precio y Ventas Predichas")
st.plotly_chart(fig_dispersion)

# Crear gráfico de barras con colores basados en las ventas predichas
df_barras = df_filtrado.groupby('Mes')['Ventas_Predichas'].sum().reset_index()

# Definir un rango de colores para las ventas
fig_barras = px.bar(df_barras, x="Mes", y="Ventas_Predichas",
                    title="Ventas Predichas por Mes",
                    color="Ventas_Predichas", 
                    color_continuous_scale="RdYlGn_r",  # Aquí se usa la escala de color rojo a verde (invertido)
                    labels={'Ventas_Predichas': 'Ventas Predichas'})
st.plotly_chart(fig_barras)

# Crear gráfico de línea
fig_linea = px.line(df_filtrado.groupby('Mes')['Ventas_Predichas'].sum().reset_index(), 
                    x="Mes", y="Ventas_Predichas", title="Ventas Predichas por Mes")
st.plotly_chart(fig_linea)
