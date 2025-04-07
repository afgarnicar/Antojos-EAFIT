from django import forms
from .models import Entrepreneur

class EntrepreneurForm(forms.ModelForm):
    class Meta:
        model = Entrepreneur
        fields = ['business_name', 'location', 'schedule', 'contact_info']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'schedule': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
        }   