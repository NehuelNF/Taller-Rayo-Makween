from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def paginaPrincipal(request):
    template = loader.get_template('paginaPrincipal.html')
    return HttpResponse(template.render({}, request))

def Carro(request):
    template = loader.get_template('Carro.html')
    return HttpResponse(template.render({}, request))

def Catalogo(request):
    template = loader.get_template('Catalogo.html')
    return HttpResponse(template.render({}, request))

def Catalogo2(request):
    template = loader.get_template('Catalogo2.html')
    return HttpResponse(template.render({}, request))

def Login(request):
    template = loader.get_template('Login.html')
    return HttpResponse(template.render({}, request))

def postulacion(request):
    template = loader.get_template('postulacion.html')
    return HttpResponse(template.render({}, request))

def Registrar(request):
    template = loader.get_template('Registrar.html')
    return HttpResponse(template.render({}, request))

def Solicitud(request):
    template = loader.get_template('Solicitud.html')
    return HttpResponse(template.render({}, request))


