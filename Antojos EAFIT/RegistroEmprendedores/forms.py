from django import forms
from .models import Entrepreneur

class EntrepreneurForm(forms.ModelForm):
    class Meta:
        model = Entrepreneur
        fields = ['business_name', 'location', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'contact_info']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'lunes': forms.TextInput(attrs={'class': 'form-control'}),
            'martes': forms.TextInput(attrs={'class': 'form-control'}),
            'miercoles': forms.TextInput(attrs={'class': 'form-control'}),
            'jueves': forms.TextInput(attrs={'class': 'form-control'}),
            'viernes': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
        }   