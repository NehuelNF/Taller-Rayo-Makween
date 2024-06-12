#from django.conf.urls import url
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.paginaPrincipal, name = 'paginaPrincipal'),
    path('Carro', views.Carro, name = 'Carro'),
    path('Catalogo', views.Catalogo, name = 'Catalogo'),
    path('Catalogo2', views.Catalogo2, name='Catalogo2'),
    path('Login', views.Login, name='Login'),
    path('postulacion', views.postulacion, name='postulacion'),
    path('Registrar', views.Registrar, name='Registrar'),
    path('Solicitud', views.Solicitud, name='Solicitud'),
]