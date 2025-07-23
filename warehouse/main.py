# from csv_handler import load_items, save_items
from repositories.item_repository import ItemRepository
from domain.models import Warehouse, Item
from os import system

clear_crt = "clear"
filename = "warehouse_inventory.csv"
repository = ItemRepository(filename)

def print_report(items):
    print(f"\n{'Item':<20} {'Quantity':<10} {'Expiration Date':<20} {'Price':<10}")
    for item in items:
        print(f"{item.name:<20} {item.quantity:<10} {item.expiration_date:<20} {item.price:<10}")

class MenuManager:
    running = True
    choice = None

    def print_menu(self):
        system(clear_crt)
        print(f"\nWarehouse Inventory Menu:\n{'=' * 25}")
        print(" 1. Add Item")
        print(" 2. Remove Item")
        print(" 3. Update Item")
        print(" 4. Get Full Report")
        print(" 5. Get Expired Items")
        print(" 6. Search Item")
        print(" 7. Sort By Expiration Date")
        print(" 8. Sort By Price")
        print(" 9. Sort By Quantity")
        print("\n 0. Quit\n")

    def get_choice(self):
        try:
            self.choice = int(input("Enter your choice: "))
        except:
            self.choice = None

    def run_choice(self):
        match self.choice:

            case 1:
                system(clear_crt)
                name = input("Item name: ")
                quantity = input("Quantity: ")
                date_str = input("Expiration Date (YYYY-MM-DD): ")
                price = input("Price: ")
                warehouse.add_item(Item(name, quantity, date_str, price))
                # save_items(filename, warehouse.items)
                repository.save_all(warehouse.items)
                print("\nItem added.")
                input("\nPress ENTER to continue.")

            case 2:
                system(clear_crt)
                name = input("Item name to remove: ")
                warehouse.remove_item(name)
                # save_items(filename, warehouse.items)
                repository.save_all(warehouse.items)
                print("\nItem removed.")
                input("\nPress ENTER to continue.")

            case 3:
                system(clear_crt)
                name = input("Item to update: ")
                quantity = input("New quantity (or blank): ")
                date_str = input("New expiration date (or blank): ")
                price = input("New price (or blank): ")
                updates = {}
                if quantity: updates["quantity"] = quantity
                if date_str: updates["expiration_date"] = date_str
                if price: updates["price"] = price
                warehouse.update_item(name, updates)
                # save_items(filename, warehouse.items)
                repository.save_all(warehouse.items)
                print("\nItem updated.")
                input("\nPress ENTER to continue.")

            case 4:
                system(clear_crt)
                print_report(warehouse.items)
                input("\nPress ENTER to continue.")

            case 5:
                system(clear_crt)
                expired = warehouse.get_expired_items()
                if expired:
                    print_report(expired)
                else:
                    print("No expired items.")
                input("\nPress ENTER to continue.")

            case 6:
                system(clear_crt)
                name = input("Search item: ")
                result = warehouse.search_item(name)
                print_report([result]) if result else print("Item not found.")
                input("\nPress ENTER to continue.")

            case 7:
                system(clear_crt)
                sorted_items = warehouse.get_sorted_items("expiration_date")
                print_report(sorted_items)
                input("\nPress ENTER to continue.")

            case 8:
                system(clear_crt)
                sorted_items = warehouse.get_sorted_items("price")
                print_report(sorted_items)
                input("\nPress ENTER to continue.")

            case 9:
                system(clear_crt)
                sorted_items = warehouse.get_sorted_items("quantity")
                print_report(sorted_items)
                input("\nPress ENTER to continue.")

            case 0:
                system(clear_crt)
                print("Exiting...")
                self.running = False

            case _:
                input("\nInvalid input! Press ENTER to try again.")

# Setup
# warehouse = Warehouse()
# warehouse.items = load_items(filename)

warehouse = Warehouse()
warehouse.items = repository.load_all()

manager = MenuManager()

while manager.running:
    manager.print_menu()
    manager.get_choice()
    manager.run_choice()
