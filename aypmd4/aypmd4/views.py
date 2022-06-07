from django.http import HttpResponse
from django.template import Template, Context
from aypmd4 import aws_config
import time 


def welcome(request):
    return HttpResponse("Pagina inicial")

def homePage(request):
    listaComunas = ["acund","la reina", "tester"] #cambiar
    listaPeriodos = ["00", "01", "02"]
    data = aws_config.AthenaQuery()
    plantillaHomePage = open("C:/Users/Chopan/Desktop/AYPMD/aypmd4/aypmd4/templates/homePage.html")
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comunas": listaComunas, "periodos": listaPeriodos, "data": data })
    documento = template.render(contexto)
    return HttpResponse(documento)

def detalleVista(request):
    #data = aws_config.AthenaQuery("hola")
    template =  "detalleVista.htlm"
    nombreComuna = request.GET["c"]
    print(nombreComuna)
    nombrePeriodo = request.GET["periodo"]
    plantillaHomePage = open("C:/Users/Chopan/Desktop/AYPMD/aypmd4/aypmd4/templates/detalleVista.html")
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comuna": nombreComuna, "periodo": nombrePeriodo})
    documento = template.render(contexto)
    return HttpResponse(documento)    

   