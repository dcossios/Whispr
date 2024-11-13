from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Reunion
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ReunionTests(APITestCase):
    def setUp(self):
        # Crear usuario y token para la prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_reunion(self):
        url = reverse('reunion-list-create')
        data = {'titulo': 'Reunión de prueba', 'fecha': '2024-11-12T10:00:00Z', 'duracion': '01:00:00'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reunion.objects.count(), 1)
        self.assertEqual(Reunion.objects.get().titulo, 'Reunión de prueba')
