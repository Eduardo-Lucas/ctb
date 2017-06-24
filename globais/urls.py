from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^empresalista', views.empresalista, name='empresa/empresalista'),
    url(r'^empresaadiciona', views.empresaadiciona, name='empresa/empresaadiciona'),
    url(r'^empresaedita', views.empresaedita, name='empresa/empresaedita'),
]
