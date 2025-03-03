# Create your views here.
from django.shortcuts import render, redirect
from .models import Entrepreneur
from .forms import EntrepreneurForm

def home(request):
    return render(request, 'home.html')

def entrepreneur_list(request):
    entrepreneurs = Entrepreneur.objects.all()
    return render(request, 'entrepreneurs.html', {'entrepreneurs': entrepreneurs})

def create_entrepreneur(request):
    if request.method == "POST":
        form = EntrepreneurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EntrepreneurForm()
    return render(request, 'create_entrepreneur.html', {'form': form})

def success(request):
    return render(request, 'success.html')
