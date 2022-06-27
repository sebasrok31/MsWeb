from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

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

def Apuntes (request):
    return render(request, "MsApuntes.html",{})

def ApuntesGet (request):
    Apuntes_Directorio={
        "10A":{
            "Matematicas":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EZTxeO-OQX1IsmUOvsgLoFoBnjmNJlnOAhyL0b03ryju1A?e=Mn6AWF",
            
            "Español":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EWynswzOrm1Hscc9vZApEsoBon3fg7TWDejsSKvwvQLi1A?e=mCvYkT",

            "Biologia":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/ET7Y46tuSxpMvCNcg0iowUwBmEr_zfE0Mr3W7yIEF0fVeA?e=CgOvoO",
            
            "Historia":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/ERukSNUHZxVGjaHJyzx14dEBzxjSS_9jI2UcaIfNf6feAA?e=UUFhBb",
            
            "Fisica":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EfSziFrxs5xOo7l2tFh7gycBCiGV3kEZnY427GQuZccZLQ?e=IzdE47",
            
            "Ingles":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/Ee9ubP64q6pOq-qUpDedvqwBxWwCKlzwyTifslPMrEvGnw?e=Kfux2r",
            
            "Quimica":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EdvmEUdRu3NFnT3faGsfbGUBqiXk2fhv-xfNA6cZxBPssg?e=3BnUFl",
            
            "TOK":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/ER1coIAO0SpBrr8o0KMs8p8BnP3E_mUcVaPj856rXPNXFg?e=D7ZUZi",
            
            "Filosofia":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EVdKyKqPjFhGsqrgmZxnfYYBb5mJsizel_mM3lY0coPj6g?e=kjzyyx",
            
            "Frances":
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EfMkejaOYnxOqhRLTdI8QCMBpNx4Tshyf1Xkz9xa66GAxg?e=umbAgT",
            
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
                "https://corgimpin-my.sharepoint.com/:w:/g/personal/roblesmorenojuansebastian_glp_edu_co/EUWmvMwxaAJMttBeK_GeElUBNh0ysbBymRJsfhS4BfQmyg?e=OLKHeR"
    }}
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
