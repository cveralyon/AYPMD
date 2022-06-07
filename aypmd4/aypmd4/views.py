from django.http import HttpResponse
from django.template import Template, Context
import aws_config


def welcome(request):
    return HttpResponse("Pagina inicial")

def homePage(request):
    listaComunas = ["acund","la reina", "tester"] #cambiar
    listaPeriodos = ["00", "01", "02"]
    plantillaHomePage = open("C:/Users/Chopan/Desktop/AYPMD/aypmd4/aypmd4/templates/homePage.html")
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comunas": listaComunas, "periodos": listaPeriodos })
    documento = template.render(contexto)
    return HttpResponse(documento)

def detalleVista(request):
    listaComunas = ["acund","la reina", "tester"] #cambiar
    listaPeriodos = ["00", "01", "02"]
    data = aws_config.AthenaQuery("hola")
    plantillaHomePage = open("C:/Users/Chopan/Desktop/AYPMD/aypmd4/aypmd4/templates/homePage.html")
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context({"comunas": listaComunas, "periodos": listaPeriodos , "data": data})
    documento = template.render(contexto)
    return HttpResponse(documento)    