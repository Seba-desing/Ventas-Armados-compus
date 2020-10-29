from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render


def venta_compu (request):
    return render(request,"pag.html")
def venta_compu2 (request):
    return render(request,"armar.html")  
def venta_compu3 (request):
    return render(request,"comprar.html")
def venta_compu4 (request):
    return render(request,"despacho.html") 
def venta_compu5 (request):
    return render(request,"finalizar.html")             

