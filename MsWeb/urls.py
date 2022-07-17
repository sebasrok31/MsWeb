"""MsWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from MsWeb.views import bienvenida, bienvenidaVerde, categoria, obtenerMomentoActual, contenidoHTML, test_plantilla, plantilla_parametros, loader_plantilla, plantillaShortcut, plantillaHija1, plantillaHija2, index_test, Menu_principal, Tareografo, Tutorias, Apuntes, buscar, ApuntesGet, PaginasDeApoyo, TutoOpGet, TutoAgGet

urlpatterns = [
    path('admin/', admin.site.urls),
    path("bienvenida/", bienvenida),
    path("Verde/", bienvenidaVerde),
    path("Edad/<int:edad>", categoria),
    path("fecha/", obtenerMomentoActual),
    path("contenidoHTML/<nombre>/<int:edad>", contenidoHTML),
    path("testplantilla/", test_plantilla),
    path("coso que no funciona/", plantilla_parametros),
    path("loader_plantilla/", loader_plantilla),
    path("plantillaShortcut/", plantillaShortcut),
    path("plantillaHija1/", plantillaHija1),
    path("plantillaHija2/", plantillaHija2),
    path("index_test/", index_test),
    path("Menu_principal/", Menu_principal),
    path("Tareografo/", Tareografo),
    path("Tutorias/", Tutorias),
    path("Apuntes/", Apuntes),
    path("buscar/", buscar),
    path("ApuntesGet/", ApuntesGet),
    path("PaginasDeApoyo/", PaginasDeApoyo),
    path("TutoOpGet/", TutoOpGet),
    path("TutoAgGet/", TutoAgGet),
    
    path("", Menu_principal),
]
