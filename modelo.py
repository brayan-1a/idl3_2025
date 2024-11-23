import streamlit as st

# Título de la aplicación
st.title('Sistema de Predicción de Inventario')

# Subtítulo explicativo
st.subheader('Consulta la cantidad de inventario necesaria para los productos.')

# Descripción de la aplicación
st.write("""
    Este sistema predice la cantidad de inventario necesaria en función de diversos factores,
    como la temperatura máxima, la cantidad de lluvia, la semana del año y la cantidad vendida.
    Puedes ingresar estos datos para obtener una estimación de la cantidad de inventario recomendada.
""")

# Sección para seleccionar el producto
st.header('Selecciona el Producto')
producto_seleccionado = st.selectbox(
    'Elige un producto de la lista:',
    ['Pepino', 'Cebolla', 'Lechuga']
)

# Sección para ingresar la temperatura máxima
st.header('Parámetros de Clima')
temperatura = st.slider(
    'Temperatura Máxima (°C):',
    min_value=10,
    max_value=40,
    value=30,
    step=1
)

# Sección para ingresar la cantidad de lluvia
lluvia = st.slider(
    'Cantidad de Lluvia (mm):',
    min_value=0.0,
    max_value=20.0,
    value=5.0,
    step=0.1
)

# Sección para ingresar la semana del año
semana = st.slider(
    'Semana del Año:',
    min_value=1,
    max_value=52,
    value=30,
    step=1
)

# Sección para ingresar la cantidad vendida
st.header('Datos de Venta')
cantidad_vendida = st.number_input(
    'Cantidad Vendida:',
    min_value=0,
    value=10,
    step=1
)

# Espacio para el botón de predicción (aún sin funcionalidad)
st.header('Predicción')
if st.button('Predecir Inventario'):
    st.write('El resultado de la predicción aparecerá aquí.')
    
# Diseño de la interfaz con un contenedor para mostrar todos los elementos de forma ordenada
st.write("""
    ## Visualización de la Predicción
    La predicción de inventario será mostrada aquí una vez que se implementen las funcionalidades.
""")

# Diseño de la estructura con algunas imágenes o iconos (opcional, para darle una mejor apariencia)
st.image("https://via.placeholder.com/800x200.png?text=Predicci%C3%B3n+de+Inventario", caption="Gráfico de Predicción de Inventario", use_column_width=True)

# Colocar los elementos en columnas para mejorar la apariencia visual
col1, col2 = st.columns(2)

with col1:
    st.subheader('Producto Seleccionado')
    st.write(f"**{producto_seleccionado}**")

with col2:
    st.subheader('Resumen de Datos Ingresados')
    st.write(f"**Temperatura Máxima:** {temperatura} °C")
    st.write(f"**Cantidad de Lluvia:** {lluvia} mm")
    st.write(f"**Semana del Año:** {semana}")
    st.write(f"**Cantidad Vendida:** {cantidad_vendida}")

# Sección de pie de página o nota adicional
st.markdown("""
    ### Nota:
    Los resultados de la predicción dependen de los datos ingresados y se ajustarán conforme se desarrolle la lógica de predicción.
    Esta aplicación se conecta con un modelo de predicción de inventario basado en las condiciones climáticas y las ventas históricas.
""")

