from django.shortcuts import render
from .models import Reunion

# Create your views here.
def lista_reuniones(request):
    return render(request, 'index.html')