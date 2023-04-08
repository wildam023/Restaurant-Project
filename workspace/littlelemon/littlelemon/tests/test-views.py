from django.test import TestCase, Client

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuItemsView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        Menu.objects.create(title="Dish1", price=15, inventory=500)
        Menu.objects.create(title="Dish2", price=25, inventory=50)
        Menu.objects.create(title="Dish3", price=150, inventory=5)

    def test_getall(self):
        response = self.client.get("restaurant/menu/")
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response, serializer.data)

    def test_getone(self):
        item = Menu.objects.create(title="DishA", price=50, inventory=25)
        response = self.client.get(f"restaurant/menu/{item.id}/")
        serializer = MenuSerializer(item, many=False)
        self.assertEqual(response.data, serializer.data)		