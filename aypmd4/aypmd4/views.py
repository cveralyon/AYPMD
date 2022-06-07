from django.http import HttpResponse
from django.template import Template, Context
from aypmd4 import aws_config
import time 
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def welcome(request):
    return HttpResponse("Pagina inicial")

def homePage(request):
    listaComunas = ["acund","la reina", "tester"] #cambiar
    listaPeriodos = ["00", "01", "02"]
    data = aws_config.AthenaQuery()
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/homePage.html')
    plantillaHomePage = open(dir)
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comunas": listaComunas, "periodos": listaPeriodos, "data": data })
    documento = template.render(contexto)
    return HttpResponse(documento)

def detalleVista(request):
    #data = aws_config.AthenaQuery("hola")
    template =  "detalleVista.htlm"
    nombreComuna = request.GET["comuna"]
    print(nombreComuna)
    nombrePeriodo = request.GET["periodo"]
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/detalleVista.html')
    plantillaHomePage = open(dir)
    
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comuna": nombreComuna, "periodo": nombrePeriodo})
    documento = template.render(contexto)
    return HttpResponse(documento)    

   