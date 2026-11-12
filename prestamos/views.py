from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

@login_required
def inicio(request):
    return render(request, 'inicio.html')

def es_encargado(user):
    return user.is_authenticated and user.is_staff

def inicio(request):
    return render(request, 'inicio.html')