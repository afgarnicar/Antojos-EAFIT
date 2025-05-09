from django.shortcuts import render, redirect, get_object_or_404
from .forms import EntrepreneurForm, ProductForm
from .models import Entrepreneur, Product
from django.http import HttpResponse
from django.core.files.storage import default_storage
from cloudinary.uploader import upload as cloudinary_upload

# Create your views here.
def create_entrepreneur(request):
    if request.method == "POST":
        form = EntrepreneurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EntrepreneurForm()
    return render(request, 'create_entrepreneur.html', {'form': form})

def delete_entrepreneur(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    if request.method == 'POST':
        entrepreneur.delete()
        return redirect('entrepreneur_list')
    return render(request, 'confirm_delete.html', {'entrepreneur': entrepreneur})

def success(request):
    return render(request, 'success.html')

def entrepreneur_list(request):
    entrepreneurs = Entrepreneur.objects.prefetch_related('products')  # Use the correct related name
    return render(request, 'entrepreneur_list.html', {'entrepreneurs': entrepreneurs})



def add_product(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse("Formulario inválido", status=400)

        # ---- Mapeo y validación de categoría ----
        category_mapping = {
            "1": "Dulcesito",
            "2": "Saladito",
            "3": "Accesorios",
            "4": "Bebidas",
            "5": "Servicios",
            "6": "Candies",
        }
        category_id = request.POST.get('category')
        category_name = category_mapping.get(category_id)
        if not category_name:
            return HttpResponse("Categoría inválida.", status=400)

        try:
            # 1) Subir la imagen a Cloudinary
            image_file = form.cleaned_data['image_file']
            result = cloudinary_upload(image_file, folder="products/")
            secure_url = result.get('secure_url')

            # 2) Crear el producto con la categoría **nombre**
            Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                category=category_name,
                entrepreneur=entrepreneur,
                image_url=secure_url
            )
            return redirect('product_success', pk=entrepreneur.pk)

        except Exception as e:
            return HttpResponse(f"Error al subir a Cloudinary: {e}", status=500)

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {
        'entrepreneur': entrepreneur,
        'form': form
    })


def view_products(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    products = Product.objects.filter(entrepreneur=entrepreneur)
    return render(request, 'view_products.html', {'entrepreneur': entrepreneur, 'products': products})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    entrepreneur = product.entrepreneur  # Get the associated entrepreneur

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            category_id = request.POST.get('category')

            category_mapping = {
                "1": "Dulcesito",
                "2": "Saladito",
                "3": "Accesorios",
                "4": "Bebidas",
                "5": "Servicios",
                "6": "Candies",
            }
            category_name = category_mapping.get(category_id, "")

            if not name or not description or not price or not category_name:
                return HttpResponse("Error: All fields except image are required.")

            # Update the product fields
            product.name = name
            product.description = description
            product.price = price
            product.category = category_name

            if image:  # Update the image only if a new one is provided
                product.image = image

            product.save()
            return redirect('view_products', pk=entrepreneur.pk)  # Redirect to the product list
        except Exception as e:
            return HttpResponse(f"Error: {e}")

    return render(request, 'edit_product.html', {'product': product, 'entrepreneur': entrepreneur})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('view_products', pk=product.entrepreneur.pk)  # Redirect to the product list
    return render(request, 'confirm_delete_product.html', {'product': product})



def product_success(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    return render(request, 'product_success.html', {'entrepreneur': entrepreneur})


def catalogo(request):
    # Group products by category
    categories = Product.objects.values_list('category', flat=True).distinct()
    categorized_products = {category: Product.objects.filter(category=category) for category in categories}

    return render(request, 'catalogo.html', {'categorized_products': categorized_products})