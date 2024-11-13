from django.urls import path
from . import views
from .views import ReunionListCreate, TranscripcionListCreate, AnalisisListCreate


urlpatterns = [
    path('', views.lista_reuniones, name='lista_reuniones'),
    path('reuniones/', ReunionListCreate.as_view(), name='reunion-list-create'),
    path('transcripciones/', TranscripcionListCreate.as_view(), name='transcripcion-list-create'),
    path('analisis/', AnalisisListCreate.as_view(), name='analisis-list-create'),
]

