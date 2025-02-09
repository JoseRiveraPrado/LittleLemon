from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        """Crea instancias de prueba de Menu antes de cada test"""
        self.client = APIClient()  # Simula peticiones a la API
        self.item1 = Menu.objects.create(title="Burger", price=10.99, inventory=50)
        self.item2 = Menu.objects.create(title="Pizza", price=8.99, inventory=30)
        self.item3 = Menu.objects.create(title="Salad", price=6.50, inventory=20)

    def test_getall(self):
        """Recupera todos los objetos del modelo Menu y verifica la respuesta"""
        response = self.client.get(reverse('menu-list'))  # Asegurar de que esta URL está definida en urls.py
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Imprimir la respuesta para ver qué devuelve la API
        print(f"DEBUG: Response Data = {response.data}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)  # Compara la API con los datos serializados