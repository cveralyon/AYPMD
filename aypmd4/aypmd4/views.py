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
    listaComunas = ["CURICO","LA REINA", "QUILPUE"] #cambiar
    listaPeriodos = ["2-2019", "1-2017", "1-2020"]
    listaRegiones = ["13", "14", "15"]
    query = type_of_filter.TypeOfFilter("","","")
    data = aws_config.AthenaQuery(query)
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/homePage.html')
    plantillaHomePage = open(dir)
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comunas": listaComunas, "periodos": listaPeriodos, "regiones": listaRegiones, "data": data })
    documento = template.render(contexto)
    return HttpResponse(documento)

def detalleVista(request):
    
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
    
    listaComunas = ["CURICO","LA REINA", "QUILPUE"] #cambiar
    listaPeriodos = ["2-2019", "1-2017", "1-2020"]
    listaRegiones = ["13", "14", "15"]
    query = type_of_filter.TypeOfFilter(nombreComuna,nombrePeriodo,nombreRegion)
    print(query)
    data = aws_config.AthenaQuery(query)
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/homePage.html')
    plantillaHomePage = open(dir)
    print("NOMBRES--")
    print(nombreComuna)
    print(nombrePeriodo)
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comuna": nombreComuna, "periodo": nombrePeriodo, "region": nombreRegion,"comunas": listaComunas, "periodos": listaPeriodos, "regiones": listaRegiones, "data": data })
    documento = template.render(contexto)
    return HttpResponse(documento)    

   