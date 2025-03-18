from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Datos
import requests

def index(request):
    # Configuración de la API
    api_key = settings.OPENWEATHERMAP_API_KEY
    ciudad = "Itagüí"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    try:
        # Realiza la solicitud a la API
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos_clima = respuesta.json()

        # Extrae los datos relevantes
        contexto = {
            'ciudad': ciudad,
            'temperatura': datos_clima['main']['temp'],
            'humedad': datos_clima['main']['humidity'],
            'descripcion': datos_clima['weather'][0]['description'],
            'icono': datos_clima['weather'][0]['icon'],
        }

    except requests.exceptions.RequestException as e:
        contexto = {'error': f"Error al obtener los datos del clima: {str(e)}"}
    except KeyError as e:
        contexto = {'error': f"Error al procesar los datos del clima: {str(e)}"}

    # Obtener los datos creados manualmente desde la base de datos
    datos_manuales = Datos.objects.all().order_by('-id')  # Ordenar por ID descendente
    contexto['datos_manuales'] = datos_manuales

    return render(request, 'clima/index.html', contexto)

def crear_datos(request):
    if request.method == 'POST':
        ciudad = request.POST.get('ciudad')
        temperatura = request.POST.get('temperatura')
        humedad = request.POST.get('humedad')

        # Crea un nuevo registro en la base de datos
        Datos.objects.create(
            ciudad=ciudad,
            temperatura=temperatura,
            humedad=humedad,
        )

        return redirect('index')  # Redirige a la página principal

    return render(request, 'clima/index.html')


def editar_datos(request, id):
    # Obtener el registro a editar
    dato = get_object_or_404(Datos, id=id)

    if request.method == 'POST':
        # Actualizar el registro con los datos del formulario
        dato.ciudad = request.POST.get('ciudad')
        dato.temperatura = request.POST.get('temperatura')
        dato.humedad = request.POST.get('humedad')
        dato.save()

        return redirect('index')  # Redirigir a la página principal después de actualizar

    # Mostrar el formulario de edición con los datos actuales
    return render(request, 'clima/editar.html', {'dato': dato})

def eliminar_datos(request, id):
    # Obtener el registro a eliminar
    dato = get_object_or_404(Datos, id=id)

    if request.method == 'POST':
        # Eliminar el registro
        dato.delete()
        return redirect('index')  # Redirigir a la página principal después de eliminar

    # Mostrar una confirmación antes de eliminar (opcional)
    return render(request, 'clima/confirmar_eliminar.html', {'dato': dato})