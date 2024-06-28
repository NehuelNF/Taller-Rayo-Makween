#from django.conf.urls import url
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.paginaPrincipal, name='paginaPrincipal'),
    path('Carro', views.Carro, name='Carro'),
    path('Catalogo', views.Catalogo, name='Catalogo'),
    path('Catalogo2', views.Catalogo2, name='Catalogo2'),
    path('Login', views.Login, name='Login'),
    path('postulacion', views.postulacion, name='postulacion'),
    path('Registrar', views.Registrar, name='Registrar'),
    path('Solicitud', views.Solicitud, name='Solicitud'),
    path('Servicio', views.Servicio, name='Servicio'),
    path('lista_mantenimientos', views.lista_mantenimientos, name='lista_mantenimientos'),
    
    
    # Catalogo
    path('A-Agua1', views.A_Agua1, name='A-Agua1'),
    path('A-Agua2', views.A_Agua2, name='A-Agua2'),
    path('A-AmortiguadorD', views.A_AmortiguadorD, name='A-AmortiguadorD'),
    path('A-AmortiguadorT', views.A_AmortiguadorT, name='A-AmortiguadorT'),
    path('A-Ampolleta', views.A_Ampolleta, name='A-Ampolleta'),
    path('A-Bateria1', views.A_Bateria1, name='A-Bateria1'),
    path('A-Bateria2', views.A_Bateria2, name='A-Bateria2'),
    path('A-Bateria3', views.A_Bateria3, name='A-Bateria3'),
    path('A-Bateria4', views.A_Bateria4, name='A-Bateria4'),
    path('A-Bieleta', views.A_Bieleta, name='A-Bieleta'),
    path('A-Bobina1', views.A_Bobina1, name='A-Bobina1'),
    path('A-Bobina2', views.A_Bobina2, name='A-Bobina2'),
    path('A-BombaAgua', views.A_BombaAgua, name='A-BombaAgua'),
    path('A-BombaAuxiliar', views.A_BombaAuxiliar, name='A-BombaAuxiliar'),
    path('A-Bujia1', views.A_Bujia1, name='A-Bujia1'),
    path('A-Bujia2', views.A_Bujia2, name='A-Bujia2'),
    path('A-Chapa', views.A_Chapa, name='A-Chapa'),
    path('A-Correa', views.A_Correa, name='A-Correa'),
    path('A-CorreaVariador', views.A_CorreaVariador, name='A-CorreaVariador'),
    path('A-Neumatico1', views.A_Neumatico1, name='A-Neumatico1'),
    path('A-Neumatico2', views.A_Neumatico2, name='A-Neumatico2'),
    path('A-Neumatico3', views.A_Neumatico3, name='A-Neumatico3'),
    path('A-Termostato1', views.A_Termostato1, name='A-Termostato1'),
    path('A-Termostato2', views.A_Termostato2, name='A-Termostato2'),

    # Administracion
    path('Menu', views.Menu, name='menu'),
    path('agregar', views.agregar, name='agregar'),
    path('listar', views.listar, name='listar'),
    path('listarM', views.listarM, name='listarM'),
    path('listarS', views.listarS, name='listarS'),
    path('mecanicos/', views.listarM, name='listarM'),
    path('modificar', views.Modificar, name='modificar'),
    path('agrega', views.agrega, name='agrega'),
]