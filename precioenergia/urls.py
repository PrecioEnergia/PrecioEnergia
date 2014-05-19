from django.conf.urls.defaults import *
from precioenergia.views import main_page, EnviarDatos

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^ObtenerDatos/$', EnviarDatos),
)