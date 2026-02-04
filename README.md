Gemini-api para poder usar una API mediante Visual Studio Code usando Gemini IA
Paso 1: Creación de carpeta y apertura de terminal

Crear una carpeta en la cual usaremos la API que vamos a desarrollar. Esta carpeta se puede crear en cualquier parte del disco, evitando crearla dentro de “Documentos”. La carpeta puede llamarse gemini-api.
Una vez creada la carpeta, abrimos Visual Studio Code y seleccionamos la carpeta que acabamos de crear. Después de esto, abrimos una nueva terminal dentro de Visual Studio Code.

Paso 2: Creación del entorno virtual
Ya estando en la terminal, crearemos un entorno virtual. Para ello usamos el siguiente comando:
En Windows:
python -m venv env

En macOS o Linux:
python3 -m venv env
Con esto se creará una carpeta llamada env, en la cual se guardarán todos los paquetes que instalemos para este proyecto.

Paso 3: Activación del entorno virtual
En la misma terminal, una vez creado el entorno virtual, debemos activarlo.
En Windows:
.\env\Scripts\Activate
En macOS o Linux:
source env/bin/activate
Para comprobar que el entorno está activo existen dos formas:
Presionar Ctrl + Shift + P, buscar Python: Select Interpreter y verificar que el intérprete seleccionado apunte a env/Scripts.
Verificar en la terminal que aparezca (env) antes de la ruta del proyecto.

Paso 4: Instalación de librerías y uso del entorno virtual
Instalaremos las librerías necesarias para trabajar con Gemini y variables de entorno usando el siguiente comando:
pip install google-genai python-dotenv
Una vez instaladas las librerías, creamos un archivo donde se guardarán todas las dependencias del proyecto ejecutando:
pip freeze > requirements.txt
Luego, creamos un archivo dentro de la carpeta del proyecto llamado prueba_entorno.py, en el cual colocaremos el siguiente código para verificar que el entorno virtual funciona correctamente y que podemos conectarnos a la API de Gemini:

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=clave_api)

def ejecutar_consulta():
print("🚀 Conectando con el motor de Gemini ...")
try:
response = client.models.generate_content(
model="gemini-3-flash-preview",
contents="Preséntate brevemente como un asistente de IA configurado para apoyar el curso de 'Desarrollo de aplicaciones con IA.'"
)

    print("\n--- Respuesta Recibida ---")  
    print(response.text)  
    print("--------------------------")  

except Exception as e:  
    print(f"❌ Ocurrió un error en la conexión: {e}")  


if name == "main":
ejecutar_consulta()

Paso 5: Creación de la API KEY y configuración de la conexión
Para obtener la API KEY, ingresamos a Google AI Studio con nuestra cuenta de Google. En la parte inferior izquierda seleccionamos la opción Get API key, luego hacemos clic en Create API key, asignamos un nombre a la clave y finalmente la creamos.

Paso 6: Configuración de variables de entorno
En la carpeta raíz del proyecto creamos un archivo llamado .env. Dentro de este archivo colocamos nuestra API KEY de la siguiente manera:
GEMINI_API_KEY=TU_API_KEY_DE_GEMINI
Después de agregar la clave, actualizamos el archivo de dependencias ejecutando nuevamente:
pip freeze > requirements.txt

Paso 7: Funcionamiento de la API de IA con Gemini
Creamos un archivo en la raíz del proyecto llamado app_gemini.py y copiamos el siguiente código:

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=clave_api)

def ejecutar_consulta():
print("🚀 Conectando con el motor de Gemini ...")
try:
response = client.models.generate_content(
model="gemini-3-flash-preview",
contents="Preséntate brevemente como un asistente de IA configurado para apoyar el curso de 'Desarrollo de aplicaciones con IA.'"
)

    print("\n--- Respuesta Recibida ---")  
    print(response.text)  
    print("--------------------------")  

except Exception as e:  
    print(f"❌ Ocurrió un error en la conexión: {e}")  


if name == "main":
ejecutar_consulta()

En este código importamos la librería google-genai, la cual utilizamos para conectarnos al modelo de Gemini, y python-dotenv, que nos permite leer la clave almacenada en el archivo .env.
Luego cargamos la variable de entorno que contiene la API KEY, inicializamos el cliente de Gemini y creamos una función que envía una petición al modelo gemini-3-flash-preview. El texto enviado corresponde al prompt, que en este caso solicita una presentación breve del asistente de IA.

<img width="1919" height="1002" alt="image" src="https://github.com/user-attachments/assets/f04dc5a3-09c0-4c77-816e-3e6287a13e1e" />
