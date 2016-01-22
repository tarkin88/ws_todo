from rest_framework import serializers

from apps.tareas.models import Tarea


class TareasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarea
