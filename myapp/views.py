from django.shortcuts import render, redirect
from .models import Mantenimiento
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.

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
    if request.method == 'POST':
        nombre = request.POST.get('usuario')
        correo = request.POST.get('email')
        contraseña = request.POST.get('pass')

        # Verificar si el correo ya existe
        if User.objects.filter(email=correo).exists():
            return render(request, 'Registrar.html', {'correo_en_uso': True})

        # Crear el objeto User y guardar en la base de datos
        nuevo_usuario = User(username=nombre, email=correo, password=make_password(contraseña))
        nuevo_usuario.save()
        
        return redirect('Login')
    return render(request, 'Registrar.html')

def Solicitud(request):
    template = loader.get_template('Solicitud.html')
    return HttpResponse(template.render({}, request))

def Servicio(request):
    if request.method == 'POST':
        mecanico = request.POST['mecanico']
        zona = request.POST['zona']
        pieza = request.POST['piezas']
        comentarios = request.POST['comentarios']

        Mantenimiento.objects.create(
            mecanico=mecanico,
            zona=zona,
            pieza=pieza,
            comentarios=comentarios
        )
        
        return HttpResponse("Mantenimiento registrado exitosamente")
    return render(request, 'Servicio.html')

def lista_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.all()
    return render(request, 'lista_mantenimientos.html', {'mantenimientos': mantenimientos})



# Definición de las vistas para cada producto del catálogo

def A_Agua1(request):
    template = loader.get_template('Catalogo/A-Agua1.html')
    return HttpResponse(template.render({}, request))

def A_Agua2(request):
    template = loader.get_template('Catalogo/A-Agua2.html')
    return HttpResponse(template.render({}, request))

def A_AmortiguadorD(request):
    template = loader.get_template('Catalogo/A-AmortiguadorD.html')
    return HttpResponse(template.render({}, request))

def A_AmortiguadorT(request):
    template = loader.get_template('Catalogo/A-AmortiguadorT.html')
    return HttpResponse(template.render({}, request))

def A_Ampolleta(request):
    template = loader.get_template('Catalogo/A-Ampolleta.html')
    return HttpResponse(template.render({}, request))

def A_Bateria1(request):
    template = loader.get_template('Catalogo/A-Bateria1.html')
    return HttpResponse(template.render({}, request))

def A_Bateria2(request):
    template = loader.get_template('Catalogo/A-Bateria2.html')
    return HttpResponse(template.render({}, request))

def A_Bateria3(request):
    template = loader.get_template('Catalogo/A-Bateria3.html')
    return HttpResponse(template.render({}, request))

def A_Bateria4(request):
    template = loader.get_template('Catalogo/A-Bateria4.html')
    return HttpResponse(template.render({}, request))

def A_Bieleta(request):
    template = loader.get_template('Catalogo/A-Bieleta.html')
    return HttpResponse(template.render({}, request))

def A_Bobina1(request):
    template = loader.get_template('Catalogo/A-Bobina1.html')
    return HttpResponse(template.render({}, request))

def A_Bobina2(request):
    template = loader.get_template('Catalogo/A-Bobina2.html')
    return HttpResponse(template.render({}, request))

def A_BombaAgua(request):
    template = loader.get_template('Catalogo/A-BombaAgua.html')
    return HttpResponse(template.render({}, request))

def A_BombaAuxiliar(request):
    template = loader.get_template('Catalogo/A-BombaAuxiliar.html')
    return HttpResponse(template.render({}, request))

def A_Bujia1(request):
    template = loader.get_template('Catalogo/A-Bujia1.html')
    return HttpResponse(template.render({}, request))

def A_Bujia2(request):
    template = loader.get_template('Catalogo/A-Bujia2.html')
    return HttpResponse(template.render({}, request))

def A_Chapa(request):
    template = loader.get_template('Catalogo/A-Chapa.html')
    return HttpResponse(template.render({}, request))

def A_Correa(request):
    template = loader.get_template('Catalogo/A-Correa.html')
    return HttpResponse(template.render({}, request))

def A_CorreaVariador(request):
    template = loader.get_template('Catalogo/A-CorreaVariador.html')
    return HttpResponse(template.render({}, request))

def A_Neumatico1(request):
    template = loader.get_template('Catalogo/A-Neumatico1.html')
    return HttpResponse(template.render({}, request))

def A_Neumatico2(request):
    template = loader.get_template('Catalogo/A-Neumatico2.html')
    return HttpResponse(template.render({}, request))

def A_Neumatico3(request):
    template = loader.get_template('Catalogo/A-Neumatico3.html')
    return HttpResponse(template.render({}, request))

def A_Termostato1(request):
    template = loader.get_template('Catalogo/A-Termostato1.html')
    return HttpResponse(template.render({}, request))

def A_Termostato2(request):
    template = loader.get_template('Catalogo/A-Termostato2.html')
    return HttpResponse(template.render({}, request))

# Administracion
def Menu(request):
    template = loader.get_template('Administracion/Menu.html')
    return HttpResponse(template.render({}, request))

