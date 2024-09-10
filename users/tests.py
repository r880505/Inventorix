from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.superuser = CustomUser.objects.create_superuser(
            username='ranggi',
            password='1qazxsw2'
        )
        
        refresh = RefreshToken.for_user(self.superuser)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        
    def test_create_user(self):
        url = reverse('user-list-create')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': '1qazxsw2'
        }
        
        response = self.client.post(url, data, format = 'json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(),2)
        self.assertEqual(CustomUser.objects.get(username = 'testuser').email,'testuser@example.com')
        
    def test_create_user_missing_required_field(self):
        url = reverse('user-list-create')
        data = {
            # 'username': 'testuser',
            # 'email' : 'testuser@example.com', # missing field
            'first_name': 'Test',
            'last_name': 'User',
            'password': '1qazxsw2'
        }
        
        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(),1)
        