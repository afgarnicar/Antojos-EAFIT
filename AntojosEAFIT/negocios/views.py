from django.shortcuts import render,get_object_or_404
from .models import Categoria, Product
from RegistroEmprendedores.models import Entrepreneur


def catalogo_view(request):
    return render(request, 'catalogo.html', {
        'emprendimientos': range(1, 21)
    })


def categorias_view(request):
    categorias = Categoria.objects.all()  # Obtén todas las categorías
    return render(request, 'categorias.html', {'categorias': categorias})


def catalogo(request):
    todos = Product.objects.all()
    return render(request, 'catalogo.html', {
        'products': todos
    })

def entrepreneur_detail(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    return render(request, 'entrepreneur_detail.html', {
        'entrepreneur': entrepreneur
    })

def product_detail(request, pk):
    product = get_object_or_404(Product.objects.select_related('entrepreneur'), pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def category_products(request, category_name):
    # Filtrar productos por la categoría seleccionada
    products = Product.objects.filter(category=category_name)

    # Debugging: Imprimir los productos filtrados
    print(f"Category: {category_name}, Products: {list(products)}")

    return render(request, 'category_products.html', {'products': products, 'category_name': category_name})

def entrepreneur_detail_carousel(request, entrepreneur_id):
    entrepreneur = get_object_or_404(Entrepreneur, pk=entrepreneur_id)
    products = Product.objects.filter(entrepreneur=entrepreneur)
    return render(request, 'entrepreneur_detail_carousel.html', {
        'entrepreneur': entrepreneur,
        'products': products
    })

def get_recommended_products():
    # For now, we'll just get the latest 12 products
    # You can modify this logic later to use different criteria for recommendations
    return Product.objects.select_related('entrepreneur').order_by('-id')[:12]

def inicio(request):
    recommended_products = get_recommended_products()
    return render(request, 'inicio.html', {
        'recommended_products': recommended_products
    })


