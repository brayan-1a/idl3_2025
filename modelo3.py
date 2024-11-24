import streamlit as st

# Título de la aplicación
st.title('Predicción de Inventario Inteligente')

# Descripción general
st.write("""
    Este sistema utiliza modelos avanzados para predecir el inventario necesario en función de datos climáticos y de ventas. 
    Ingresa la información requerida y explora los resultados visuales.
""")

# Dividir la página en dos columnas
col1, col2 = st.columns(2)

# Primera columna: Datos de Entrada
with col1:
    st.subheader("🔍 Datos de Entrada")
    producto = st.selectbox("Producto:", ["Pepino", "Cebolla", "Lechuga"])
    temp = st.slider("Temperatura Máxima (°C):", 10, 40, 25, 1)
    lluvia = st.slider("Cantidad de Lluvia (mm):", 0.0, 20.0, 3.0, 0.1)
    semana = st.slider("Semana del Año:", 1, 52, 15, 1)
    ventas = st.number_input("Cantidad Vendida:", min_value=0, value=5, step=1)

# Segunda columna: Botón y resultados
with col2:
    st.subheader("⚙️ Resultado de Predicción")
    st.write("Presiona el botón para obtener una predicción.")
    if st.button("Predecir"):
        st.write("La predicción aparecerá aquí (pendiente de implementación).")
    else:
        st.write("Esperando datos para la predicción.")

# Separador
st.markdown("---")

# Bloque de visualización gráfica
st.header("📊 Gráficos de Predicción")
st.image("https://via.placeholder.com/600x200.png?text=Gr%C3%A1fico+de+Predicci%C3%B3n", use_column_width=True)
st.write("Los resultados se visualizarán aquí una vez implementada la funcionalidad.")
