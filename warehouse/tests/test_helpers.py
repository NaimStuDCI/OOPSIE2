import unittest
from unittest.mock import patch
from io import StringIO
from datetime import date
from domain.models import Item, Warehouse
import helpers

class TestHelpers(unittest.TestCase):

    @patch('builtins.input')
    def test_input_item_valid(self, mock_input):
        # Simulate user input for a valid item
        mock_input.side_effect = [
            "Orange",        # name
            "15",            # quantity
            "12.34",         # price
            "2025-10-10"     # expiration_date
        ]
        existing_names = ["Apple", "Banana"]
        item = helpers.input_item(existing_names)
        self.assertEqual(item.name, "Orange")
        self.assertEqual(item.quantity, 15)
        self.assertEqual(item.price, 12.34)
        self.assertEqual(item.expiration_date, date(2025, 10, 10))

    @patch('builtins.input')
    def test_input_item_invalid_name_then_valid(self, mock_input):
        # Simulate invalid then valid name input
        mock_input.side_effect = [
            "",              # invalid empty
            "123Invalid",    # invalid characters
            "Apple",         # already exists
            "NewItem",       # valid name
            "5",             # quantity
            "9.99",          # price
            "2023-01-01"     # expiration_date
        ]
        existing_names = ["Apple", "Banana"]
        with patch('builtins.print') as mock_print:
            item = helpers.input_item(existing_names)
            self.assertEqual(item.name, "NewItem")
            self.assertEqual(item.quantity, 5)
            # Check print called with expected error messages
            mock_print.assert_any_call("Name cannot be empty.")
            mock_print.assert_any_call("Name can only contain letters and spaces.")
            mock_print.assert_any_call("An item with this name already exists.")

    @patch('builtins.input')
    def test_input_item_updates_valid_and_invalid(self, mock_input):
        warehouse = Warehouse()
        warehouse.items.append(Item("Apple", 10, date(2023, 1, 1), 5.5))
        existing_names = [item.name for item in warehouse.items]

        # Inputs: item to update, quantity (valid), price (invalid), expiration_date (invalid)
        mock_input.side_effect = [
            "Apple",     # item to update
            "20",       # new quantity valid
            "-10",      # invalid price (negative)
            "invalid"   # invalid date
        ]
        with patch('builtins.print') as mock_print:
            name, updates = helpers.input_item_updates(existing_names, warehouse)
            self.assertEqual(name, "Apple")
            self.assertEqual(updates.get("quantity"), 20)
            self.assertNotIn("price", updates)  # invalid price ignored
            self.assertNotIn("expiration_date", updates)  # invalid date ignored

            # Check error prints for invalid price and date
            mock_print.assert_any_call("Invalid price. Keeping old value.")
            mock_print.assert_any_call("Invalid date format. Keeping old value.")

    def test_print_report_output(self):
        items = [
            Item("TestItem1", 5, date(2023, 5, 1), 10.0),
            Item("TestItem2", 2, date(2024, 6, 2), 20.555)
        ]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            helpers.print_report(items)
            output = mock_stdout.getvalue()
            # Check headers and one item's details appear in output
            self.assertIn("Item", output)
            self.assertIn("Quantity", output)
            self.assertIn("Expiration Date", output)
            self.assertIn("Price", output)
            self.assertIn("TestItem1", output)
            self.assertIn("5", output)
            self.assertIn("2023-05-01", output)
            self.assertIn("10.00", output)  # price formatted 2 decimals
            self.assertIn("TestItem2", output)
            self.assertIn("20.55", output)  # price rounded/displayed 2 decimals

if __name__ == "__main__":
    unittest.main()
