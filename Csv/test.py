from django.test import TestCase
from mainApp.models import Item
from decimal import Decimal
class ItemModelTest(TestCase):
    def setUp(self):
        Item.objects.create(
            name="Test Item",
            code="12345",
            price=Decimal('99.99'),
            quantity=10,
            vendor="Test Vendor",
        )

    def test_item_creation(self):
        item = Item.objects.get(name="Test Item")
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.code, "12345")
        self.assertEqual(item.vendor, "Test Vendor")
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.price, Decimal('99.99'))
