from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'home.html')

def registro_view(request):
    return render(request, 'register.html')