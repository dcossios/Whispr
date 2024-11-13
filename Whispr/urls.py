from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.lista_reuniones, name='lista_reuniones'),
]
