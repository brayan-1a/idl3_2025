#1. Importar las librerías
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from supabase import create_client, Client

#2. Configurar Supabase
SUPABASE_URL = "https://beryfdwrzvykxrnnshxa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJlcnlmZHdyenZ5a3hybm5zaHhhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI2Nzc3MTUsImV4cCI6MjA0ODI1MzcxNX0.4gCYexJCUYQHEWYj2J5CceKSNvBXqC3SxwNT8fBE9cU"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

#3. Función para cargar datos desde Supabase
@st.cache_data
def fetch_data():
    response = supabase.table("students_data").select("*").execute()
    data = pd.DataFrame(response.data)
    return data

#4. Interfaz Streamlit
st.title("Modelo de Predicción de Aprobación de Examen")

#5. Cargando y mostrando datos
data = fetch_data()
if data.empty:
    st.warning("No hay datos en la base de datos. Por favor, inserta datos primero.")
else:
    st.write("Datos cargados desde Supabase:")
    st.dataframe(data)

#6. Preprocesamiento de datos
X = data[['asistencia', 'horas_estudio']]  # Variables de entrada
y = data['aprobo']  # Variable objetivo

#7. División de los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#8. Entrenar el modelo de Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

#9. Evaluación del modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Precisión del modelo: {accuracy:.2f}")

#10. Predicción personalizada
asistencia = st.number_input("Asistencia (%)", min_value=0, max_value=100, value=85)
horas_estudio = st.number_input("Horas de estudio por semana", min_value=0, max_value=40, value=10)

input_data = pd.DataFrame({
    "asistencia": [asistencia],
    "horas_estudio": [horas_estudio]
})

prediction = model.predict(input_data)[0]
st.write("¿Aprobará el examen?", "Sí" if prediction else "No")
