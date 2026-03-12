from django.test import TestCase
from decimal import Decimal
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Salad", price=9.99, inventory=20)

    def test_getall(self):
        iceCream = Menu.objects.get(title="IceCream")
        salad = Menu.objects.get(title="Salad")
        self.assertEqual(iceCream.price, 80.00)
        self.assertEqual(iceCream.inventory, 100)
        self.assertEqual(salad.price, Decimal("9.99"))
        self.assertEqual(salad.inventory, 20)
