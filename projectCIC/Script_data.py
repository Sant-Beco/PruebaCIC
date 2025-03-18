import os
import requests
import schedule
import time
from django.core.wsgi import get_wsgi_application
from django.conf import settings

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectCIC.settings')  # Cambia 'tu_proyecto' por 'projectCIC'
application = get_wsgi_application()

from clima.models import Datos  # Importa el modelo Datos

# Configuración de la API
API_KEY = settings.OPENWEATHERMAP_API_KEY
CIUDAD = "Itagüí"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CIUDAD}&appid={API_KEY}&units=metric&lang=es"

def fetch_weather_data():
    try:
        # Realiza la solicitud a la API
        respuesta = requests.get(URL)
        respuesta.raise_for_status()
        datos_clima = respuesta.json()

        # Extrae los datos relevantes
        temperatura = datos_clima['main']['temp']
        humedad = datos_clima['main']['humidity']

        # Guarda los datos en la base de datos
        Datos.objects.create(
            ciudad=CIUDAD,
            temperatura=temperatura,
            humedad=humedad,
        )
        print(f"Datos guardados: {CIUDAD}, Temp: {temperatura}°C, Hum: {humedad}%")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos del clima: {str(e)}")
    except KeyError as e:
        print(f"Error al procesar los datos del clima: {str(e)}")

# Programa la tarea para que se ejecute cada minuto
schedule.every(1).minutes.do(fetch_weather_data)

# Bucle para ejecutar las tareas programadas
if __name__ == "__main__":
    print("Iniciando el script de descarga de datos del clima...")
    while True:
        schedule.run_pending()
        time.sleep(1)