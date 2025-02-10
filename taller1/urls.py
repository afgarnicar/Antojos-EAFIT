
from django.contrib import admin
from django.urls import path,include
from cuentas import views


urlpatterns = [
   
    path('', include('cuentas.urls')),
    path('admin/', admin.site.urls),
]
