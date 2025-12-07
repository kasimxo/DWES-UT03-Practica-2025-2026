from django.db import models

# Create your models here.
class Tarea(models.Model):
    id = models.UUIDField(primary_key=True) # UUID de ejemplo: 42536292-a95b-422f-a411-d877c260022e
    titulo = models.CharField()
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_recordatorio = models.DateTimeField()

    def __str__(self):
        return self.titulo