
# from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [
    path('', views.publish_product, name='publish_product'),
    path('categories/', views.categories, name='categories'),
]