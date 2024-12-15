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
# Establecer fondo y borde para el gráfico de dispersión
fig_dispersion.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente para el área del gráfico
    paper_bgcolor='rgba(255,255,255,0.9)',  # Fondo blanco para el cuadro del gráfico
    margin=dict(t=40, b=40, l=40, r=40),  # Márgenes alrededor del gráfico
    font=dict(color='black'),  # Color de la fuente del gráfico
    title=dict(font=dict(color='black'))  # Color del título
)
st.plotly_chart(fig_dispersion)

# Crear gráfico de barras con colores basados en las ventas predichas
df_barras = df_filtrado.groupby('Mes')['Ventas_Predichas'].sum().reset_index()

# Definir un rango de colores para las ventas
fig_barras = px.bar(df_barras, x="Mes", y="Ventas_Predichas",
                    title="Ventas Predichas por Mes",
                    color="Ventas_Predichas", 
                    color_continuous_scale="RdYlGn_r",  # Aquí se usa la escala de color rojo a verde (invertido)
                    labels={'Ventas_Predichas': 'Ventas Predichas'})
# Establecer fondo y borde para el gráfico de barras
fig_barras.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente para el área del gráfico
    paper_bgcolor='rgba(255,255,255,0.9)',  # Fondo blanco para el cuadro del gráfico
    margin=dict(t=40, b=40, l=40, r=40),  # Márgenes alrededor del gráfico
    font=dict(color='black'),  # Color de la fuente del gráfico
    title=dict(font=dict(color='black'))  # Color del título
)
st.plotly_chart(fig_barras)

# Crear gráfico de línea
fig_linea = px.line(df_filtrado.groupby('Mes')['Ventas_Predichas'].sum().reset_index(), 
                    x="Mes", y="Ventas_Predichas", title="Ventas Predichas por Mes")
# Establecer fondo y borde para el gráfico de línea
fig_linea.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente para el área del gráfico
    paper_bgcolor='rgba(255,255,255,0.9)',  # Fondo blanco para el cuadro del gráfico
    margin=dict(t=40, b=40, l=40, r=40),  # Márgenes alrededor del gráfico
    font=dict(color='black'),  # Color de la fuente del gráfico
    title=dict(font=dict(color='black'))  # Color del título
)
st.plotly_chart(fig_linea)
