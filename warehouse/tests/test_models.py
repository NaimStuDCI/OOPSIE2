import unittest
from datetime import date

from domain.models import Item, Warehouse


class TestItem(unittest.TestCase):
    def test_is_expired_true(self):
        item = Item("milk", expiration_date=date(2000, 1, 1))
        self.assertTrue(item.is_expired(today=date(2023, 1, 1)))

    def test_is_expired_false(self):
        item = Item("yogurt", expiration_date=date(2099, 12, 31))
        self.assertFalse(item.is_expired(today=date(2023, 1, 1)))

    def test_update_values(self):
        item = Item("soda", quantity=5, expiration_date=date(2023, 8, 1), price=1.50)
        item.update(quantity=10, price=2.0)
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.price, 2.0)
        self.assertEqual(item.expiration_date, date(2023, 8, 1))


class TestWarehouse(unittest.TestCase):
    def setUp(self):
        self.wh = Warehouse()
        self.item1 = Item("apple", quantity=5, expiration_date=date(2023, 1, 1), price=0.5)
        self.item2 = Item("banana", quantity=10, expiration_date=date(2026, 1, 1), price=0.3)
        self.wh.add_item(self.item1)
        self.wh.add_item(self.item2)

    def test_add_existing_item_raises(self):
        with self.assertRaises(ValueError):
            self.wh.add_item(Item("apple"))

    def test_remove_item(self):
        self.wh.remove_item("apple")
        self.assertIsNone(self.wh.search_item("apple"))

    def test_update_item(self):
        self.wh.update_item("banana", {"price": 1.2})
        item = self.wh.search_item("banana")
        self.assertEqual(item.price, 1.2)

    def test_get_expired_items(self):
        expired = self.wh.get_expired_items()
        self.assertEqual(len(expired), 1)
        self.assertEqual(expired[0].name, "apple")

    def test_sort_by_price(self):
        sorted_items = self.wh.get_sorted_items(sort_key=lambda x: x.price)
        self.assertEqual(sorted_items[0].name, "banana")
        self.assertEqual(sorted_items[1].name, "apple")

    def test_get_occupancy(self):
        warehouse = Warehouse()
        assert warehouse.get_occupancy() == 0

        warehouse.add_item(Item("monitor"))
        warehouse.add_item(Item("keyboard"))
        assert warehouse.get_occupancy() == 2

        warehouse.remove_item("monitor")
        assert warehouse.get_occupancy() == 1


if __name__ == '__main__':
    unittest.main()
