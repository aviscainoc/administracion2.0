"""administracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aprobadas/', views.aprobadas, name="aprobadas"),
    path('pendientes/', views.pendientes, name="pendientes"),
    path('productos/', views.productos, name="productos"),
    path('servicios/', views.servicios, name="servicios"),
    path('reportesEfectivo/', views.reportesEfectivo, name="reportesEfectivo"),
    path('reportesTCredito/', views.reportesTCredito, name="reportesTCredito"),
    path('usuarios/', views.usuarios, name="usuarios"),

    path('pendientes/editarEmpresa/<int:id>',views.editarEmpresa, name="editarEmpresa"),
    path('aprobadas/editarEmpresa/<int:id>',views.editarEmpresa, name="editarEmpresa"),

    path('productos/editarProductoServicio/<int:id>',views.editarProductoServicio, name="editarProductoServicio"),
    path('servicios/editarProductoServicio/<int:id>',views.editarProductoServicio, name="editarProductoServicio"),


    path('crearEmpresa/',views.crearEmpresa, name="crearEmpresa"),
    path('crearProductoServicio/',views.CrearProductos, name="crearProducto"),

    path('admin/', admin.site.urls),
]
