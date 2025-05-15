from django.shortcuts import render
from negocios.models import Product

def inicio(request):
    recommended_products = Product.objects.select_related('entrepreneur').order_by('-id')[:12]
    return render(request, 'inicio.html', {
        'recommended_products': recommended_products
    })
