from django.shortcuts import render, redirect
from .forms import EntrepreneurForm
from .models import Entrepreneur

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

def success(request):
    return render(request, 'success.html')

def entrepreneur_list(request):
    entrepreneurs = Entrepreneur.objects.all()
    return render(request, 'entrepreneur_list.html', {'entrepreneurs': entrepreneurs})