from django.urls import path
from .views import busqueda_view, search_api

urlpatterns = [
    path('busqueda/', busqueda_view, name='busqueda_view'),
    path('api/search-products/', search_api, name='search_products_api'),
]