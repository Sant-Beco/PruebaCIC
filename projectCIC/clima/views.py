from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Datos
import requests
import pandas as pd
import plotly.express as px
import plotly.io as pio

def obtener_datos_clima(ciudad):
    """Obtiene los datos climáticos de la API de OpenWeatherMap."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric&lang=es"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()

        return {
            "ciudad": ciudad,
            "temperatura": datos["main"]["temp"],
            "humedad": datos["main"]["humidity"],
            "descripcion": datos["weather"][0]["description"],
            "icono": datos["weather"][0]["icon"],
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Error al obtener los datos del clima: {str(e)}"}
    except KeyError as e:
        return {"error": f"Error al procesar los datos del clima: {str(e)}"}

def index(request):
    """Vista principal que muestra los datos climáticos y los registros de la base de datos."""
    ciudad_filtro = request.GET.get("ciudad_filtro", "")  # Obtener el valor del filtro

    if ciudad_filtro:
        datos_manuales = Datos.objects.filter(ciudad__icontains=ciudad_filtro).order_by("-id")
    else:
        datos_manuales = Datos.objects.all().order_by("-id")

    contexto = obtener_datos_clima("Itagüí")
    contexto["datos_manuales"] = datos_manuales
    contexto["ciudad_filtro"] = ciudad_filtro  # Para mantener el valor en el formulario

    return render(request, "clima/index.html", contexto)

def crear_datos(request):
    """Crea un nuevo registro en la base de datos."""
    if request.method == "POST":
        Datos.objects.create(
            ciudad=request.POST.get("ciudad"),
            temperatura=request.POST.get("temperatura"),
            humedad=request.POST.get("humedad"),
        )
        return redirect("index")

    return render(request, "clima/index.html")

def editar_datos(request, id):
    """Edita un registro existente."""
    dato = get_object_or_404(Datos, id=id)

    if request.method == "POST":
        dato.ciudad = request.POST.get("ciudad")
        dato.temperatura = request.POST.get("temperatura")
        dato.humedad = request.POST.get("humedad")
        dato.save()
        return redirect("index")

    return render(request, "clima/editar.html", {"dato": dato})

def eliminar_datos(request, id):
    """Elimina un registro de la base de datos."""
    dato = get_object_or_404(Datos, id=id)

    if request.method == "POST":
        dato.delete()
        return redirect("index")

    return render(request, "clima/confirmar_eliminar.html", {"dato": dato})

def generar_grafico():
    """Genera un gráfico con los datos de temperatura y humedad por ciudad."""
    queryset = Datos.objects.values("ciudad", "temperatura", "humedad")
    df = pd.DataFrame(list(queryset))

    if df.empty:
        return None

    df_grouped = df.groupby("ciudad", as_index=False).mean()

    fig = px.bar(
        df_grouped,
        x="ciudad",
        y=["temperatura", "humedad"],
        barmode="group",
        title="Temperatura y Humedad Promedio por Ciudad",
        labels={"value": "Valor", "variable": "Parámetro", "ciudad": "Ciudad"},
    )

    return pio.to_html(fig, full_html=False)

def graficos(request):
    """Renderiza la vista con el gráfico generado."""
    grafico_html = generar_grafico()

    contexto = {"grafico_html": grafico_html} if grafico_html else {"mensaje": "No hay datos suficientes para generar el gráfico."}

    return render(request, "clima/graficos.html", contexto)
