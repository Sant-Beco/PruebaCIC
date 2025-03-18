import os
import requests
import schedule
import time
import logging
from django.core.wsgi import get_wsgi_application
from django.conf import settings

# Configura el entorno de Django para poder acceder a los modelos y la configuración del proyecto.
# Esto es necesario porque el script no se ejecuta dentro del contexto normal de Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectCIC.settings')
application = get_wsgi_application()

# Importa el modelo `Datos` desde la aplicación `clima` para poder guardar los datos en la base de datos.
from clima.models import Datos

# Configuración de la API de OpenWeatherMap.
# La clave API se obtiene de la configuración de Django (settings.py).
# La ciudad se puede configurar mediante una variable de entorno, con un valor predeterminado de "Itagüí".
API_KEY = settings.OPENWEATHERMAP_API_KEY
CIUDAD = os.getenv('CIUDAD', 'Itagüí')  # Ciudad configurable
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CIUDAD}&appid={API_KEY}&units=metric&lang=es"

# Configuración de logging para registrar mensajes de información y errores.
# Esto ayuda a monitorear el comportamiento del script.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_weather_data():
    """
    Función que obtiene los datos del clima desde la API de OpenWeatherMap
    y los guarda en la base de datos.
    """
    try:
        # Realiza una solicitud HTTP GET a la API de OpenWeatherMap.
        respuesta = requests.get(URL)
        respuesta.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa.
        datos_clima = respuesta.json()  # Convierte la respuesta JSON en un diccionario de Python.

        # Extrae la temperatura y la humedad del diccionario de datos.
        temperatura = datos_clima['main']['temp']
        humedad = datos_clima['main']['humidity']

        # Crea un nuevo registro en la base de datos con los datos obtenidos.
        Datos.objects.create(
            ciudad=CIUDAD,
            temperatura=temperatura,
            humedad=humedad,
        )
        # Registra un mensaje de información indicando que los datos se guardaron correctamente.
        logger.info(f"Datos guardados: {CIUDAD}, Temp: {temperatura}°C, Hum: {humedad}%")

    except requests.exceptions.RequestException as e:
        # Registra un error si hay un problema con la solicitud HTTP.
        logger.error(f"Error al obtener los datos del clima: {str(e)}")
    except KeyError as e:
        # Registra un error si no se encuentran las claves esperadas en la respuesta JSON.
        logger.error(f"Error al procesar los datos del clima: {str(e)}")

# Configura el intervalo de tiempo entre ejecuciones de la función `fetch_weather_data`.
# El intervalo se puede configurar mediante una variable de entorno, con un valor predeterminado de 1 minuto.
INTERVALO = int(os.getenv('INTERVALO', 1))  # Intervalo en minutos
schedule.every(INTERVALO).minutes.do(fetch_weather_data)

# Bucle principal del script.
# Este bucle mantiene el script en ejecución y ejecuta las tareas programadas.
if __name__ == "__main__":
    logger.info("Iniciando el script de descarga de datos del clima...")
    while True:
        schedule.run_pending()  # Ejecuta las tareas programadas.
        time.sleep(1)  # Espera 1 segundo antes de verificar nuevamente.