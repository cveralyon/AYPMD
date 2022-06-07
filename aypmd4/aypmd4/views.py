from traceback import print_tb
from django.http import HttpResponse
from django.template import Template, Context
from aypmd4 import aws_config, type_of_filter
import time 
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def welcome(request):
    return HttpResponse("Pagina inicial")

def homePage(request):
    listaComunas = ["acund","la reina", "tester"] #cambiar
    listaPeriodos = ["00", "01", "02"]
    listaRegiones = ["ARICA", "METROPOL", "VALPARAISO"]
    data = aws_config.AthenaQuery()
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/homePage.html')
    plantillaHomePage = open(dir)
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comunas": listaComunas, "periodos": listaPeriodos, "regiones": listaRegiones, "data": data })
    documento = template.render(contexto)
    return HttpResponse(documento)

def detalleVista(request):
    #data = aws_config.AthenaQuery("hola")
    template =  "detalleVista.htlm"
    try:
        nombreComuna = request.GET["comuna"]
    except:
        nombreComuna = ""

    try:
        nombrePeriodo = request.GET["periodo"]
    except:
        nombrePeriodo = ""

    try:
        nombreRegion = request.GET["region"]
    except:
        nombreRegion = ""    
    
    query = type_of_filter.TypeOfFilter(nombreComuna,nombrePeriodo)
    print(query)
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/detalleVista.html')
    plantillaHomePage = open(dir)
    print("NOMBRES--")
    print(nombreComuna)
    print(nombrePeriodo)
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comuna": nombreComuna, "periodo": nombrePeriodo, "region": nombreRegion})
    documento = template.render(contexto)
    return HttpResponse(documento)    

   