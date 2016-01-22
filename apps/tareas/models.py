from django.db import models


class Tarea(models.Model):
    PRIORIDADES = (
        (1, 'Baja'),
        (2, 'Normal'),
        (3, 'Urgente'),
        (4, 'Especial'),
    )
    ESTATUS = (
        (1, 'Incompleta'),
        (2, 'Completada'),
        (3, 'Espera'),
    )
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    prioridad = models.IntegerField(choices=PRIORIDADES, default=1)
    estatus = models.IntegerField(choices=ESTATUS, default=1)
    fecha_creacion = models.DateTimeField(auto_created=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tareas'

    def __str__(self):
        return '%s' % self.nombre
