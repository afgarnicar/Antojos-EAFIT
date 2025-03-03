from django.urls import path
from .views import entrepreneur_list, create_entrepreneur, success

urlpatterns = [
    path('emprendedores/', entrepreneur_list, name='entrepreneur_list'),
    path('crear-emprendedor/', create_entrepreneur, name='create_entrepreneur'),
    path('registro-exitoso/', success, name ='success'),
]
