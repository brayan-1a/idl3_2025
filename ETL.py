import pandas as pd
import time
from supabase import create_client, Client


url = "https://adfoiwetcaqxzdudmbsz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFkZm9pd2V0Y2FxeHpkdWRtYnN6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA4NTk5NzcsImV4cCI6MjA0NjQzNTk3N30.W7b6z-leiI_igua5iND3FcoHaF5iGTjRf_DSBP0UDRg"
supabase: Client = create_client(url, key)

csv_path = r"C:\Users\BRAYAN\Downloads\ventas_cafe.csv"


#Función para cargar datos a Supabase
def cargar_datos():
    try:
        #Leer el CSV
        df = pd.read_csv(csv_path)
        data = df.to_dict(orient="records")

        #Inserta cada registro a supabase
        for row in data:
            response = supabase.table("ventas_cafe").insert(row).execute()
            if response.data:
                print("Dato insertado", row)
            else:
                print("Error al insertar: ", response)
        print("Datos cargados exitosamente.")
    except Exception as e:
        print("Ocurrió un error al cargar los datos:", e)

#Ejecuta el proceso cada 5 min
if __name__ == "__main__":
    while True:
        cargar_datos()
        print("Esperando 5 min para la próxima carga")
        time.sleep(300)