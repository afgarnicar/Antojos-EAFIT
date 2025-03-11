from django.shortcuts import render, redirect
from .forms import ProductForm

def categories(request):
    return render(request, 'categories.html')

def publish_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            print("Form is valid and data is saved.")
            print("Saved product:", product)
            return redirect('publish_product')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = ProductForm()
    return render(request, 'publishProduct.html', {'form': form})