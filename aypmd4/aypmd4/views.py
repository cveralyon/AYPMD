from django.http import HttpResponse
from django.template import Template, Context


def welcome(request):
    return HttpResponse("Pagina inicial")

def homePage(request):
    plantillaHomePage = open("C:/Users/Chopan/Desktop/AYPMD/aypmd4/aypmd4/templates/homePage.html")
    template = Template(plantillaHomePage.read())
    plantillaHomePage.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)