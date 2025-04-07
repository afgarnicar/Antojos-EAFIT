from django.urls import path,include
from .views import create_entrepreneur, success, entrepreneur_list

urlpatterns = [
path('crear-emprendedor/', create_entrepreneur, name='create_entrepreneur'),
path('registro-exitoso/', success, name='success'),
path('emprendedores/', entrepreneur_list, name='entrepreneur_list'),
]