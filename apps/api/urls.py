from django.conf.urls import url
from .views import TareaAPIList

urlpatterns = [
    url(r'^tareas/$', TareaAPIList.as_view(), name='tareas'),

]
