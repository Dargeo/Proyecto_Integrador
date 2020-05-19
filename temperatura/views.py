from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def temperatura(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        codigoSensor = request.GET['codigoSensor']
        tipo = request.GET['tipo']
        origen = request.GET['origen']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': tipo, 'value': value, 'codigoSensor': codigoSensor, 'origen':origen}
            response = requests.post('http://127.0.0.1:8000/temperatura/', args)
            # Convierte la respuesta en JSON
            temperatura_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/temperatura/')
    # Convierte la respuesta en JSON
    temperaturas = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temperatura/temperatura.html", {'temperaturas': temperaturas})
# Create your views here.
