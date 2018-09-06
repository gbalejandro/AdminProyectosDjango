"""desarrollodoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from core.views import index, ProyectoListView, ProyectoDetailView, ProyectoCreate, ProyectoUpdate, ProyectoDelete, \
DesarrolloUpdate, DesarrolloCreate, DesarrolloDelete, busqueda

urlpatterns = [
    url(r'^$', index, name='index'),
    path('proyectos/', login_required(ProyectoListView.as_view()), name='proyectos'),
    path('proyecto/<int:pk>/', login_required(ProyectoDetailView.as_view()), name='proyecto-detail'),
    path('create/', login_required(ProyectoCreate.as_view()), name='proyecto_create'),
    path('nuevodesarrollo/<int:proyecto_id>/', login_required(DesarrolloCreate.as_view()), name='desarrollo_create'),
    path('editarproyecto/<int:pk>/', login_required(ProyectoUpdate.as_view()), name='proyecto_update'),
    path('editardesarrollo/<int:pk>/', login_required(DesarrolloUpdate.as_view()), name='desarrollo_update'),
    path('eliminar/<int:pk>/', login_required(ProyectoDelete.as_view()), name='proyecto_delete'),
    path('eliminardesarrollo/<int:pk>/', login_required(DesarrolloDelete.as_view()), name='desarrollo_delete'),
    url(r'^filtro/$', busqueda, name='proyecto_busqueda'),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
