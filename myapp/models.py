from django.db import models

class Mantenimiento(models.Model):
    mecanico = models.CharField(max_length=255)
    zona = models.CharField(max_length=255)
    pieza = models.CharField(max_length=255)
    comentarios = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)  # Campo para registrar fecha y hora en el momento de envío de formulario

    def __str__(self):
        return f"{self.mecanico} - {self.zona}"
