from os import system

from domain.models import Warehouse
from helpers import input_item, input_item_updates, print_report
from repositories.csv_repository import ItemRepository


SORT_KEYS = {
    "price": lambda x: x.price,
    "quantity": lambda x: x.quantity,
    "expiration_date": lambda x: x.expiration_date
}

clear_crt = "clear"
filename = "warehouse_inventory.csv"
repository = ItemRepository(filename)

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
                existing_names = [item.name for item in warehouse.items]
                item = input_item(existing_names)
                warehouse.add_item(item)
                repository.save_all(warehouse.items)
                print("\nItem added.")
                input("\nPress ENTER to continue.")

            case 2:
                system(clear_crt)
                name = input("Item name to remove: ")
                warehouse.remove_item(name)
                repository.save_all(warehouse.items)
                print("\nItem removed.")
                input("\nPress ENTER to continue.")

            case 3:
                system(clear_crt)
                existing_names = [item.name for item in warehouse.items]
                name, updates = input_item_updates(existing_names, warehouse)
                if name:
                    warehouse.update_item(name, updates)
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
                sorted_items = warehouse.get_sorted_items(sort_key=SORT_KEYS["expiration_date"])
                print_report(sorted_items)
                input("\nPress ENTER to continue.")

            case 8:
                system(clear_crt)
                sorted_items = warehouse.get_sorted_items(sort_key=SORT_KEYS["price"])
                print_report(sorted_items)
                input("\nPress ENTER to continue.")

            case 9:
                system(clear_crt)
                sorted_items = warehouse.get_sorted_items(sort_key=SORT_KEYS["quantity"])
                print_report(sorted_items)
                input("\nPress ENTER to continue.")

            case 0:
                system(clear_crt)
                print("Exiting...")
                self.running = False

            case _:
                input("\nInvalid input! Press ENTER to try again.")


# Setup
warehouse = Warehouse()
warehouse.items = repository.load_all()
manager = MenuManager()

while manager.running:
    manager.print_menu()
    manager.get_choice()
    manager.run_choice()
