from django.http import JsonResponse
from django.shortcuts import render
from RegistroEmprendedores.models import Product
from django.urls import reverse

def busqueda_view(request):
    return render(request, 'busqueda.html')


def search_api(request):
    query = request.GET.get('q', '')
    if len(query) > 2:
        products = Product.objects.filter(
            name__icontains=query
        ).select_related('entrepreneur')[:10]
        
        results = [{
            'id': p.id,
            'name': p.name,
            'price': float(p.price),
            'image_url': p.image_url or '',
            'category': p.category,
            'detail_url': reverse('product_detail', args=[p.id]),  # Esto generará /product/12/
            'description': p.description[:100] + '...' if p.description else '',
        } for p in products]
        
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)