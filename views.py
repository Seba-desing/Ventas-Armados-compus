from django.http import HttpResponse
from django.template import Template,Context
def bienvenida(request):
    pagina = """<html>
  <head>

  </head>
  <body>
    <h1>hoal mundo</h1>
    <button type='button' name='button'>boton1</button>
    <button type='button' name='button'>boton2</button>
  </body>
</html>"""
    return(HttpResponse(pagina))

def pagina_principal (request):
    nombre = "Pedrito"
    apellido = "Guzman"
    pagina = open("C:/dwy/proyecto1/proyecto1/HTML/index.html")
    plt = Template(pagina.read())
    pagina.close()
    ctx = Context({"var_nombre":nombre,"var_apellido":apellido})
    retorno = plt.render(ctx)
    return(HttpResponse(retorno))
def venta_compu (request):
    nombre = "Pedrito"
    apellido = "Guzman"
    pagina = open("C:/dwy\proyecto1/proyecto1/HTML/pag.html")
    plt = Template(pagina.read())
    pagina.close()
    ctx = Context({"var_nombre":nombre,"var_apellido":apellido})
    retorno = plt.render(ctx)
    return(HttpResponse(retorno))
def venta_compu2 (request):
    nombre = "Pedrito"
    apellido = "Guzman"
    pagina = open("C:/dwy\proyecto1/proyecto1/HTML/armar.html")
    plt = Template(pagina.read())
    pagina.close()
    ctx = Context({"var_nombre":nombre,"var_apellido":apellido})
    retorno = plt.render(ctx)
    return(HttpResponse(retorno))  
def venta_compu3 (request):
    nombre = "Pedrito"
    apellido = "Guzman"
    pagina = open("C:/dwy\proyecto1/proyecto1/HTML/comprar.html")
    plt = Template(pagina.read())
    pagina.close()
    ctx = Context({"var_nombre":nombre,"var_apellido":apellido})
    retorno = plt.render(ctx)
    return(HttpResponse(retorno))
def venta_compu4 (request):
    nombre = "Pedrito"
    apellido = "Guzman"
    pagina = open("C:/dwy\proyecto1/proyecto1/HTML/despacho.html")
    plt = Template(pagina.read())
    pagina.close()
    ctx = Context({"var_nombre":nombre,"var_apellido":apellido})
    retorno = plt.render(ctx)
    return(HttpResponse(retorno)) 
def venta_compu5 (request):
    nombre = "Pedrito"
    apellido = "Guzman"
    pagina = open("C:/dwy\proyecto1/proyecto1/HTML/finalizar.html")
    plt = Template(pagina.read())
    pagina.close()
    ctx = Context({"var_nombre":nombre,"var_apellido":apellido})
    retorno = plt.render(ctx)
    return(HttpResponse(retorno))             

