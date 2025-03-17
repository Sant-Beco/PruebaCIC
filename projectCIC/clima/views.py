import requests
from django.shortcuts import render
from .models import datos
# from .forms import datosForm

# Create your views here.




def index(request):
    api_key="d49a168dac4137f9c5c7f44d4720156d"
    ciudad="medellin"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    respuesta = requests.get(url).json()

    contexto={
        'ciudad':ciudad,
        'temperatura': respuesta['main']['temp'],
        'humidity': respuesta['main']['humidity'],

    }

    return render(request,'clima/index.html')




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