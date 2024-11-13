from django.shortcuts import render
from .models import Reunion
from rest_framework import generics
from .models import Reunion, Transcripcion, Analisis
from .serializers import ReunionSerializer, TranscripcionSerializer, AnalisisSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
def lista_reuniones(request):
    return render(request, 'index.html')

#API views
class ReunionPagination(PageNumberPagination):
    page_size = 5  # Número de resultados por página

class ReunionListCreate(generics.ListCreateAPIView):
    queryset = Reunion.objects.all()
    serializer_class = ReunionSerializer

class TranscripcionListCreate(generics.ListCreateAPIView):
    queryset = Transcripcion.objects.all()
    serializer_class = TranscripcionSerializer

class AnalisisListCreate(generics.ListCreateAPIView):
    queryset = Analisis.objects.all()
    serializer_class = AnalisisSerializer