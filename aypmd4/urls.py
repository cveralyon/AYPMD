"""aypmd4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aypmd4.views import welcome
from aypmd4.views import homePage
from aypmd4.views import graficoTerrenos
from aypmd4.views import graficoAvaluo
from aypmd4.views import graficoTipo

from aypmd4.views import detalleVista
from aypmd4.views import comparación
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage),
    path('terrenos/', graficoTerrenos),
    path('avaluo/', graficoAvaluo),
    path('tipo/', graficoTipo),
    path('homePage/',detalleVista, name='busqueda'),
    path('detalleVista/',comparación, name='comparacion')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
