from django.test import TestCase
from .models import MenuItem

class MenuItemTest(TestCase):
    def test_menu_item_creation(self):
        item = MenuItem.objects.create(title="Pizza", price=9.99, inventory=10)
        self.assertEqual(item.title, "Pizza")
