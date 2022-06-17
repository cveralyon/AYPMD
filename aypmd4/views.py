from traceback import print_tb
from django.http import HttpResponse
from django.template import Template, Context
from aypmd4 import aws_config, type_of_filter, graficos

import pandas as pd
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
    graf(data)
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/homePage.html')
    plantillaHomePage = open(dir)
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comunas": listaComunas, "periodos": listaPeriodos, "regiones": listaRegiones, "data": data , "dir": dir})
    documento = template.render(contexto)
    return HttpResponse(documento)

def grafico(request):
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/terrenos.html')
    plantillaHomePage = open(dir)
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    return HttpResponse()

def graf(datos):
    sup_construida = []
    sup_terreno = []
    avaluo = []
    tipo_terreno = []
    print(datos)
    for linea in datos.values():
        if(linea[4] != ''):
            sup_terreno.append(float(linea[4]))
        else:
            sup_terreno.append(0)
        if(linea[5] != ''):
            sup_construida.append(float(linea[5]))
        else:
            sup_construida.append(0)
        avaluo.append(int(linea[1])/1500)
        tipo_terreno.append(linea[6])
    data = pd.DataFrame()
    data['sup_construida'] = sup_construida
    data['sup_terreno'] = sup_terreno
    graficos.grafico_linea(data)
    data = pd.DataFrame()
    data['sup_terreno'] = sup_terreno
    data['avaluo'] = avaluo
    graficos.grafico_avaluo(data)
    data = pd.DataFrame()
    data['sup_terreno'] = sup_terreno
    data['tipo_terreno'] = tipo_terreno
    graficos.grafico_tipo_terreno(data)

    
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
    graf(data)
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/homePage.html')
    plantillaHomePage = open(dir)
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
    dir = os.path.join(BASE_DIR, 'aypmd4/templates/detalleVista.html')
    plantillaHomePage = open(dir)
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comuna1": nombreComuna1, "comuna2": nombreComuna2, "avgComuna1": avgComuna1, "avgComuna2": avgComuna2})
    documento = template.render(contexto)
    return HttpResponse(documento) 


   