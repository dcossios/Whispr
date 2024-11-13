# whispr/serializers.py
from rest_framework import serializers
from .models import Reunion, Transcripcion, Analisis

class ReunionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reunion
        fields = '__all__'

class TranscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcripcion
        fields = '__all__'

class AnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analisis
        fields = '__all__'
