import requests
from django.shortcuts import render
from django.conf import settings
from .models import Datos
from django.conf import settings

def index(request):
    # Configuración de la API
    api_key = settings.OPENWEATHERMAP_API_KEY  # Usa settings para manejar la API key
    ciudad = "Itagüí"  # Puedes hacerla dinámica (por ejemplo, desde un formulario)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    try:
        # Realiza la solicitud a la API
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        datos_clima = respuesta.json()

        # Extrae los datos relevantes
        contexto = {
            'ciudad': ciudad,
            'temperatura': datos_clima['main']['temp'],
            'humedad': datos_clima['main']['humidity'],
            'descripcion': datos_clima['weather'][0]['description'],
            'icono': datos_clima['weather'][0]['icon'],
        }

        # Guarda los datos en la base de datos (opcional)
        Datos.objects.create(
            ciudad=ciudad,
            temperatura=contexto['temperatura'],
            humedad=contexto['humedad'],
        )

    except requests.exceptions.RequestException as e:
        # Manejo de errores de la solicitud HTTP
        contexto = {
            'error': f"Error al obtener los datos del clima: {str(e)}"
        }
    except KeyError as e:
        # Manejo de errores si la API devuelve una estructura inesperada
        contexto = {
            'error': f"Error al procesar los datos del clima: {str(e)}"
        }

    # Renderiza la plantilla con el contexto
    return render(request, 'clima/index.html', contexto)




# def list(request):
#     datos = datos.objects.all()
#     return render(request, 'clima/index.html', {'datos': datos})



# def formulario(request):
#     if request.method == 'POST':
#         ciudad = request.POST['ciudad']
#         temperatura = request.POST['temperatura']
#         humedad = request.POST['humedad']

#         datos = datos(
#             ciudad=ciudad,
#             temperatura=temperatura,
#             humedad=humedad,
#         )
#         datos.save()
#         return redirect('index')
#     return render(request, 'clima/index.html')