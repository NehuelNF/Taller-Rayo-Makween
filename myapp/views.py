from django.shortcuts import render, redirect
from .models import Mantenimiento, Mecanico
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .decorators import staff_required, superuser_required
from django.contrib.auth.decorators import login_required


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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('menu')  # Redirigir a la página del menú para el personal
            else:
                return redirect('paginaPrincipal')  # Redirigir a la página principal para otros usuarios
        else:
            if not User.objects.filter(username=username).exists():
                messages.error(request, 'Usuario inexistente')
            else:
                messages.error(request, 'Contraseña incorrecta')
    return render(request, 'Login.html')

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

@login_required
@staff_required
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
    else:
        mecanicos = Mecanico.objects.all()
        return render(request, 'Administracion/Servicio.html', {'mecanicos': mecanicos})

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

@login_required
@superuser_required
def Menu(request):
    template = loader.get_template('Administracion/menu.html')
    return HttpResponse(template.render({}, request))


@login_required
@superuser_required
def agregar(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        aPaterno = request.POST['paterno']
        aMaterno = request.POST['materno']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']

        Mecanico.objects.create(        rut = rut,
                                        nombre = nombre,
                                        apellido_paterno=aPaterno,
                                        apellido_materno=aMaterno,
                                        telefono=telefono,
                                        email=email,
                                        direccion=direccion,
                                        )
    return render(request, 'Administracion/agregar.html')

@login_required
@superuser_required
def listar(request):
    mecanico=Mecanico.objects.all()
    context={"mecanico":Mecanico}
    return render(request, 'Administracion/listar.html', context)


def listarM(request):
    mecanicos = Mecanico.objects.all()
    contexto = {
        'mecanicos': mecanicos
    }
    return render(request, 'Administracion/listarM.html', contexto)

def listarS(request):
    Servicios = Mantenimiento.objects.all()
    contexto = {
        'Servicios': Servicios
    }
    return render(request, 'Administracion/listarS.html', contexto)

def Modificar(request):
    template = loader.get_template('Administracion/Modificar.html')
    return HttpResponse(template.render({}, request))

def ModificarM(request):
    template = loader.get_template('Administracion/ModificarM.html')
    return HttpResponse(template.render({}, request))

def ModificarM(request):
    mecanicos = Mecanico.objects.all()
    contexto = {
        'mecanicos': mecanicos
    }
    return render(request, 'Administracion/ModificarM.html', contexto)

def agrega(request):
    template = loader.get_template('Administracion/agrega.html')
    return HttpResponse(template.render({}, request))

def Rechazado(request):
    template = loader.get_template('Rechazado.html')
    return HttpResponse(template.render({}, request))

def mecanicos_findEdit(request,pk):
    if pk != "":
        mecanico=Mecanico.objects.get(rut=pk)
        context={'mecanico':mecanico}
        if mecanico:
            return render(request, 'Administracion/editM.html', context)
        else:
            context={'mensaje':'Error, rut no existe...'}
            return render(request, 'Administracion/listarM.html', context)

def mecanicos_del(request,pk):
    context={}
    try:
        mecanico=Mecanico.objects.get(rut=pk)
        mecanico.delete()
        mensaje="Bien, datos aliminados..."
        mecanico = Mecanico.objects.all()
        context = {'mecanico':mecanico, 'mensaje':mensaje }
        return render(request, 'Administracion/listarM.html', context)
    except:
        mensaje="Error, rut no existe..."
        mecanico = Mecanico.objects.all()
        context = {'mecanico': mecanico, 'mensaje': mensaje}
        return render(request, 'Administracion/listarM.html', context)

def mecanicosUpdate(request):
    if request.method == "POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        mecanico = Mecanico()
        mecanico.rut=rut
        mecanico.nombre=nombre
        mecanico.apellido_paterno=aPaterno
        mecanico.apellido_materno=aMaterno
        mecanico.telefono=telefono
        mecanico.email=email
        mecanico.direccion=direccion
        mecanico.save()
        context={'mensaje':"Ok, datos actualizados...",'mecanico':mecanico}
        return render(request, 'Administracion/editM.html', context)
    else:
        mecanico = Mecanico.objects.all()
        context= {'mecanico':mecanico}
        return render(request, 'Administracion/editM.html', context)