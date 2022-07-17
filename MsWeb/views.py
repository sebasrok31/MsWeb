from __future__ import print_function

from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
import pygsheets

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
from google.oauth2 import service_account

def bienvenida(request):
    return HttpResponse("Hello world")

def bienvenidaVerde(request):
    return HttpResponse("<p style='color: green;'>Hello world</p>")

def categoria(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "tas cucho"
        else:
            categoria = "adulto irresponsable"
    else:
        if edad < 10: 
            categoria = "ta chikito"
        else:
            categoria = "meh"
    resultado = "<h1>Categoria de la edad: %s </h1>" %categoria
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    #respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
    respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A%d%m/%Y%H:%M:%S"))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p>Nombre: %s / Edad: %s</p>
    </body
    </html>
    """% ( nombre, edad )
    return HttpResponse(contenido)

def test_plantilla(request):
    #abrir la plantilla
    plantillaexterna = open("MsWeb/templates/test.html")
    #leer plantilla
    template = Template(plantillaexterna.read())
    #cerrar plantilla
    plantillaexterna.close()
    # crear contexto
    contexto = Context()
    #renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantilla_parametros(request):
    nombre = "Sebrob"
    fechaActual = datetime.datetime.now()
    lenguajes = ["python", "ruby", "JavaScript", "Java", "C#", "kotlin"]
    #abrir la plantilla
    plantillaexterna = open("MsWeb/templates/plantilla_parametros.html")
    #leer plantilla
    template = Template(plantillaexterna.read())
    #cerrar plantilla
    plantillaexterna.close()
    # crear contexto
    contexto = Context({"nombreCanal":nombre, "fechaActual": fechaActual, "lenguajes":lenguajes})
    #renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

def loader_plantilla(request):
    nombre = "Sebrob"
    fechaActual = datetime.datetime.now()
    lenguajes = ["python", "ruby", "JavaScript", "PHP", "Java", "C#", "kotlin"]
    """
    la ruta de las plantillas se especifica en el archivo settings en la lista de las direcciones
    
    estas cargando el documento en la linea 78"
    """
    plantillaExterna = loader.get_template("plantilla_parametros.html")
    documento = plantillaExterna.render({"nombreCanal":nombre, "fechaActual": fechaActual, "lenguajes":lenguajes})
    return HttpResponse(documento)

def plantillaShortcut(request):
    nombre = "Sebrob"
    fechaActual = datetime.datetime.now()
    lenguajes = ["python", "ruby", "JavaScript", "C++" ,"PHP", "Java", "C#", "kotlin"]
    
    return render(request, "plantilla_parametros.html", {"nombreCanal":nombre, "fechaActual": fechaActual, "lenguajes":lenguajes})

def plantillaHija1(request):
    return render(request, "plantillaHija_1.html", {})

def plantillaHija2(request):
    return render(request, "plantillaHija_2.html", {})

def index_test(request):
    return render(request, "index.html",{})

def Menu_principal(request):
    return render(request, "MsMenu.html",{})

def Tareografo (request):
    return render(request, "MsTareografo.html",{})

def Tutorias (request):
    return render(request, "MsTutorias.html",{})

def TutoOpGet(request):
    Curso_Get = request.GET["Curso"]
    Opcion_Get = request.GET["Opcion"]
    
    if Curso_Get == "10A" and Opcion_Get == "Calendario":
        url="https://calendar.google.com/calendar/u/0?cid=a2NwNDFodDIyMXRkbXVrcWc0aWZnbnRsNXNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ"
        return HttpResponseRedirect(url)
    if Curso_Get == "10B" and Opcion_Get == "Calendario":
        url="https://calendar.google.com/calendar/u/0?cid=ZXI0Y2p0bTQycWFna2MzanZhOHIxN2c1djhAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ"
        return HttpResponseRedirect(url)
    if Curso_Get == "10C" and Opcion_Get == "Calendario":
        url="https://calendar.google.com/calendar/u/0?cid=cTdoOTRpZnR0OXRwNWdxM2plZm5idnFybGNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ"
        return HttpResponseRedirect(url)

    if Opcion_Get == "Agendar tutoria":
        return render(request, "MsTutoAg.html",{})
    
    if Opcion_Get == "Opcion":
        return render(request, "MsTutorias.html",{})

def TutoAgGet(request):
    Nombre_Get = request.GET["Nombre"]
    Dia_Get = request.GET["Dia"]
    Hora_Get = request.GET["hora"]
    Materia_Get = request.GET["Materia"]
    Asunto_Get = request.GET["Asunto"]
    Curso_Get = request.GET["curso"]
    
    SERVICE_ACCOUNT_FILE = "MsWeb\service_account.json"
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    Id = "1_KmpVTs5EtAFgE5fwwbe1kfwANKH7GbCMUJTS4MQevY"

    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
        
    DeltaTime = datetime.timedelta(minutes=30)
    Hora = (Hora_Get + ":00")
    DiaIni = (Dia_Get + " " + Hora)

    formato = "%Y-%m-%d %H:%M:%S"

    DiaTran = datetime.datetime.strptime(DiaIni, formato)

    Diasum = DiaTran+DeltaTime

    DiaIniT = datetime.datetime.strftime(DiaTran, "%m/%d/%Y %H:%M:%S")
    DiaFint = datetime.datetime.strftime(Diasum, "%m/%d/%Y %H:%M:%S")

    DiaInif = str(DiaIniT)
    DiaFin = str(DiaFint)

    data = [[DiaInif, DiaFin, Nombre_Get, Materia_Get, None, None, Asunto_Get]]
    res = sheet.values().append(spreadsheetId=Id,
                                range=(Curso_Get+"!A2:G99"), valueInputOption="USER_ENTERED",
                                insertDataOption="INSERT_ROWS", body={"values":data}).execute()
        
    return HttpResponseRedirect("/Tutorias/")
    
    

def Apuntes (request):
    return render(request, "MsApuntes.html",{})

def ApuntesGet (request):
    Apuntes_Directorio={
        "10A":{
            "Matematicas":
                "https://drive.google.com/drive/folders/14ekHinLMcQL_DVz663x47H7wq8qpcM2A?usp=sharing",
            
            "Español":
                "https://drive.google.com/drive/folders/1oK9HnRCLeRwYK0BikCaNzsZ_XqNMNGPC?usp=sharing",

            "Biologia":
                "https://drive.google.com/drive/folders/1PC4POJ5b8RA3kt36fbKfq47RsJ4bdG4q?usp=sharing",
            
            "Historia":
                "https://drive.google.com/drive/folders/15GicgKRvXpoJhZWYCF4edU2NI1xWrV7c?usp=sharing",
            
            "Fisica":
                "https://drive.google.com/drive/folders/1zAqkTepQWCKEbyx9HwSAKqzhgScq7Kkj?usp=sharing",
            
            "Ingles":
                "https://drive.google.com/drive/folders/1qhYmi40AMScp8Ut3MAPZmo5UocoIkIPs?usp=sharing",
            
            "Quimica":
                "https://drive.google.com/drive/folders/1lg7WbiLNSZwYVLLKazvTFg7xUQX0zEL_?usp=sharing",
            
            "TOK":
                "https://drive.google.com/drive/folders/1ByoF_iz5x6f5w7vmdfHlssBngfGRED_b?usp=sharing",
            
            "Filosofia":
                "https://drive.google.com/drive/folders/1R2CYrYMq8aDmYXXf8IZLMiAHU8Cskjtl?usp=sharing",
            
            "Frances":
                "https://drive.google.com/drive/folders/1zEqtB0skBa_pCLar7hZNjcrJDudzden-?usp=sharing",
            
        },"10B":{
            "Matematicas":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EddWViKWbQlDgDqMEio0_rABDXwgxBgiJ8PLe5AekvJ40g?e=aKdvIh",
            
            "Español":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/Ed0sRgk9bcNGsaPBTGA2N88BqJyiLMpZGnpLdJ3OOTIjlQ?e=S4ebdn",
            
            "Biologia":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EU_3q-lnxtJHpYk-YvE_DQgBvzzDK6PSUC9S8CttUgNBJQ?e=zdJ6JZ",
            
            "Historia":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/ETXdm6PmYMhFurmgKeOaTa8BVuzY3X2WOPZ7iFR0gHUkYg?e=zYiVGq",
            
            "Fisica":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EcpSOEP5umVDi-uE5UbEhNUBJmwDJk-wEOwHG4ceZpoIdw?e=WwnD5j",
            
            "Ingles":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EWF0K7YqUMNAu889xpAxs94BZ6wIrl_qzg83WmhZyQ83uA?e=xIilqO",
            
            "Quimica":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EdvtR-FllZhIo5yEuvH-plMB9jrPgMoeI8wghvIVOJ_K7Q?e=6A8DhJ",
            
            "TOK":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/Eb5BZv24K3dEl5ZLGP1LC9gBK2-iwTEO918evt6t5EzAyw?e=y2P4qw",
            
            "Filosofia":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EQk07m7I6oRBmeOlQkA8ckgBu2Tb-Kiwqff1IR-z0epj8g?e=4V1cOF",
            
            "Frances":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EUk5PkWTvrRMpclAVzW6IA0B8Fv676F7yED9hFd7zZlO8w?e=ju0iHk"
        
        }, "10C":{
            "Matematicas":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EZMU3ReXB7hOtMxGZ3d01dsBbNW9ENT4uVRNDWYjJoUuYw?e=NCXS4W",
            
            "Español":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EYydozkji79LjpnPcazfOMkBVAJoLZnAim82VI-Wu6Lr_A?e=ZJum3X",
            
            "Biologia":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EdPOwKc1yllJt3pVrwilIwYBBzj-amN9H0A4RlDqlOPGyg?e=FbN1B9",
            
            "Historia":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EUnZ283v8olBnsnCNid93HUB2JGZgk7XP5GPskh3KKeOiw?e=QLfOky",
            
            "Fisica":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EalugDcRhfJEmPShfpFl--IB3kZ-99-VNVX6e5nNHeNLvg?e=cgP7tn",
            
            "Ingles":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EerjvPqkeQFJvIN8ldq-A4sBNFDHCR-VYrDJNM7u6WJnlA?e=MaUPC0",
            
            "Quimica":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EemCvJpSgzxGpTSrncMN14oBLP6rziNXe_OM-xQ8AtEFVg?e=jKr5ES",
            
            "TOK":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EaSi6k3tJ09Hl3a6ZQiVZSoB6RkUfGMgarDYOHg-i8FCWQ?e=4fhq9f",
            
            "Filosofia":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EXTUqFJgI1RPgalXYntlcCwBboyDJXF3BhHtT3kTrzAtog?e=Rwdaex",
            
            "Frances":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EUWmvMwxaAJMttBeK_GeElUBNh0ysbBymRJsfhS4BfQmyg?e=OLKHeR"}
    }
    Curso_Get = request.GET["Curso"]
    Materia_Get = request.GET["Materia"]
    
    Dir_Curso=Apuntes_Directorio[Curso_Get]
    url=Dir_Curso[Materia_Get]
    
    return HttpResponseRedirect(url)
    
def buscar (request):
    mensaje = "articulo buscado: %r" %request.GET["prd"]
    return HttpResponse(mensaje)

def PaginasDeApoyo(request):
    return render(request, "MsPaginasDeApoyo.html",{})
