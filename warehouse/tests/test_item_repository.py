import unittest
import tempfile
import os
from datetime import date
from repositories.item_repository import ItemRepository
from domain.models import Item

class TestItemRepository(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='')
        self.temp_file.close()  # Will open as needed with repository

        # Prepare test data
        self.items = [
            Item(name="apple", quantity=10, expiration_date=date(2025, 8, 1), price=1.50),
            Item(name="banana", quantity=5, expiration_date=date(2025, 8, 11), price=0.80),
        ]
        self.repo = ItemRepository(self.temp_file.name)

    def tearDown(self):
        os.unlink(self.temp_file.name)

    def test_save_and_load_all(self):
        self.repo.save_all(self.items)
        loaded_items = self.repo.load_all()
        self.assertEqual(len(loaded_items), 2)
        self.assertEqual(loaded_items[0].name, "apple")
        self.assertEqual(loaded_items[1].quantity, 5)
        self.assertEqual(loaded_items[0].expiration_date, date(2025, 8, 1))
        self.assertAlmostEqual(loaded_items[1].price, 0.80)

    def test_save_all_overwrites_file(self):
        self.repo.save_all(self.items)
        # Save empty list should clear file
        self.repo.save_all([])
        loaded_items = self.repo.load_all()
        self.assertEqual(len(loaded_items), 0)

if __name__ == '__main__':
    unittest.main()
