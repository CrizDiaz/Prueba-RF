from django.conf.urls import url, include
from django.urls import path

from apps.adopcion.views import adoptar, SolicitudList, SolicitudCreate, SolicitudUpdate

urlpatterns = [
    url(r'^$', adoptar),
    url(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitud/nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),
    #url(r'^solicitud/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path(r'solicitud/editar/<pk>/', SolicitudUpdate.as_view(), name='solicitud_listar')
]
