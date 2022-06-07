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
    listaComunas = aws_config.GetComunas() #cambiar
    listaPeriodos = aws_config.GetPeriodo()
    listaRegiones = aws_config.GetRegiones()
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
    
    listaComunas = aws_config.GetComunas() #cambiar
    listaPeriodos = aws_config.GetPeriodo()
    listaRegiones = aws_config.GetRegiones()
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


def comparación(request):
        
    template =  "detalleVista.htlm"
    try:
        nombreComuna1 = request.GET["comuna1"]
    except:
        nombreComuna1 = ""

    try:
        nombreComuna2 = request.GET["comuna2"]
    except:
        nombreComuna2 = ""

    query = type_of_filter.CreateQueryComparacion(nombreComuna1)
    avgComuna1 = aws_config.AvgAvaluoFiscal(query)
    query = type_of_filter.CreateQueryComparacion(nombreComuna2)
    avgComuna2 = aws_config.AvgAvaluoFiscal(query)
    #listaPeriodos = ["2-2019", "1-2017", "1-2020"]
    #istaRegiones = ["13", "14", "15"]
    #query = type_of_filter.TypeOfFilter(nombreComuna,nombrePeriodo,nombreRegion)
    #print(query)
    #data = aws_config.AthenaQuery(query)
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/detalleVista.html')
    plantillaHomePage = open(dir)
    print("NOMBRES--")
    #print(nombreComuna)
    #print(nombrePeriodo)
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comuna1": nombreComuna1, "comuna2": nombreComuna2, "avgComuna1": avgComuna1, "avgComuna2": avgComuna2})
    documento = template.render(contexto)
    return HttpResponse(documento) 


   