"""
URL configuration for JobMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from CVGenerator import views as VIEWS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VIEWS.home, name='home'),
    path('register/', VIEWS.register, name='register'),
    path('login/', VIEWS.loginPage, name='login'),
    path('logout/', VIEWS.logoutUser, name='logout'),
    path('download/', VIEWS.download_docx, name='download_cv'),
    
    # Vacantes
    path('vacante/desarrollador-full-stack/', VIEWS.desarrollador_full_stack, name='desarrollador_full_stack'),
    path('vacante/administrador-proyectos/', VIEWS.administrador_proyectos, name='administrador_proyectos'),
    path('vacante/abogado-corporativo/', VIEWS.abogado_corporativo, name='abogado_corporativo'),
    path('vacante/limpiador-profesional/', VIEWS.limpiador_profesional, name='limpiador_profesional'),
    path('vacante/desarrollador-backend/', VIEWS.desarrollador_backend, name='desarrollador_backend'),
    path('vacante/asistente-administrativo/', VIEWS.asistente_administrativo, name='asistente_administrativo'),
    path('vacante/gerente-proyectos/', VIEWS.gerente_proyectos, name='gerente_proyectos'),
    path('vacante/contador-publico/', VIEWS.contador_publico, name='contador_publico'),
    path('vacante/ingeniero-devops/', VIEWS.ingeniero_devops, name='ingeniero_devops'),
    path('vacante/recepcionista/', VIEWS.recepcionista, name='recepcionista'),
    path('vacante/diseno-grafico/', VIEWS.diseno_grafico, name='diseno_grafico'),
    path('vacante/analista-datos/', VIEWS.analista_datos, name='analista_datos'),
    path('vacante/analista-recursos-humanos/', VIEWS.analista_recursos_humanos, name='analista_recursos_humanos'),
    path('vacante/ingeniero-soporte-tecnico/', VIEWS.ingeniero_soporte_tecnico, name='ingeniero_soporte_tecnico'),
    path('vacante/auxiliar-almacen/', VIEWS.auxiliar_almacen, name='auxiliar_almacen'),
    path('vacante/diseno-ux-ui/', VIEWS.diseno_ux_ui, name='diseno_ux_ui'),
]
