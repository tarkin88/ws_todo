from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^valhalla/', admin.site.urls, name='valhalla'),
    url(r'^api/', include('apps.api.urls'), name='api'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
