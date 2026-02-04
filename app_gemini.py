import os
# variable de gemini
from google import genai
# para cargar variables de entorno desde un archivo .env
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el cliente
client = genai.Client(api_key=clave_api)

def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...")
    try:
        # 3. Llamada directa al servicio de modelos
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Presentame brevemente como un programado junior puede mejorar sus habilidades en aplicaciones con IA.'"
        )

        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")

    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_consulta()
