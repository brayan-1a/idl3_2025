import streamlit as st

# Título de la aplicación
st.title('Sistema de Predicción de Inventario')

# Descripción general
st.write("""
    Bienvenido al sistema de predicción de inventario. 
    Utiliza los parámetros disponibles para consultar la cantidad de inventario necesaria 
    en función de las condiciones climáticas y ventas históricas.
""")

# Pestañas para organizar la interfaz
tab1, tab2, tab3 = st.tabs(["Datos de Entrada", "Predicción", "Visualización"])

# Tab 1: Datos de Entrada
with tab1:
    st.header("Introduce los datos para la predicción")
    
    producto_seleccionado = st.selectbox(
        'Selecciona un producto:',
        ['Pepino', 'Cebolla', 'Lechuga']
    )
    temperatura = st.slider('Temperatura Máxima (°C):', 10, 40, 30, 1)
    lluvia = st.slider('Cantidad de Lluvia (mm):', 0.0, 20.0, 5.0, 0.1)
    semana = st.slider('Semana del Año:', 1, 52, 30, 1)
    cantidad_vendida = st.number_input('Cantidad Vendida:', min_value=0, value=10, step=1)

# Tab 2: Predicción
with tab2:
    st.header("Resultados de la Predicción")
    st.write("Una vez implementada, la predicción aparecerá aquí.")
    st.button("Predecir Inventario")

# Tab 3: Visualización
with tab3:
    st.header("Gráficos y Análisis")
    st.image("https://via.placeholder.com/800x300.png?text=Visualizaci%C3%B3n+de+Predicci%C3%B3n", use_column_width=True)
    st.write("Aquí se mostrarán gráficos con los resultados de la predicción.")
