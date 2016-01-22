from django.db.models import Q
from rest_framework.generics import ListAPIView

from apps.tareas.models import Tarea
from .serializers import TareasSerializers


class TareaAPIList(ListAPIView):
    serializer_class = TareasSerializers

    def get_queryset(self):
        queryset = Tarea.objects.all()
        return queryset

    def filter_queryset(self, queryset):
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(
                    Q(nombre__icontains=q) |
                    Q(descripcion__icontains=q)
            )
        return queryset
