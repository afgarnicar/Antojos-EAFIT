from django import forms
from .models import Entrepreneur

class EntrepreneurForm(forms.ModelForm):
    class Meta:
        model = Entrepreneur
        fields = ['business_name', 'location', 'schedule', 'contact_info']
