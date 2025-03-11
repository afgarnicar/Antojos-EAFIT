from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'images']
        widgets = {
            'images': forms.ClearableFileInput(attrs={'multiple': True}),
        }
        labels = {
            'name': 'Nombre',
            'price': 'Precio',
            'category': 'Categoría',
            'images': 'Imágenes del producto',
        }