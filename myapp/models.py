from django.db import models

class Mantenimiento(models.Model):
    id = models.AutoField(primary_key=True)
    mecanico = models.CharField(max_length=255)
    zona = models.CharField(max_length=255)
    pieza = models.CharField(max_length=255)
    comentarios = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)  # Campo para registrar fecha y hora en el momento de envío de formulario

    def __str__(self):
        return f"{self.mecanico} - {self.zona}"
class User(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Mecanico(models.Model):

    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)