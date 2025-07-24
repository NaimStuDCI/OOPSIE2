from os import system

from helpers import input_item, input_item_updates, print_report


class MenuManager:
    def __init__(self, warehouse, repository, sort_keys, clear_command="clear"):
        self.warehouse = warehouse
        self.repository = repository
        self.sort_keys = sort_keys
        self.clear_command = clear_command
        self.running = True
        self.choice = None

    def print_menu(self):
        system(self.clear_command)
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
        except ValueError:
            self.choice = None

    def run_choice(self):
        match self.choice:
            case 1:
                system(self.clear_command)
                existing_names = [item.name for item in self.warehouse.items]
                item = input_item(existing_names)
                self.warehouse.add_item(item)
                self.repository.save_all(self.warehouse.items)
                print("\nItem added.")
                input("\nPress ENTER to continue.")

            case 2:
                system(self.clear_command)
                name = input("Item name to remove: ")
                self.warehouse.remove_item(name)
                self.repository.save_all(self.warehouse.items)
                print("\nItem removed.")
                input("\nPress ENTER to continue.")

            case 3:
                system(self.clear_command)
                existing_names = [item.name for item in self.warehouse.items]
                name, updates = input_item_updates(existing_names, self.warehouse)
                if name:
                    self.warehouse.update_item(name, updates)
                    self.repository.save_all(self.warehouse.items)
                    print("\nItem updated.")
                input("\nPress ENTER to continue.")

            case 4:
                system(self.clear_command)
                print_report(self.warehouse.items)
                input("\nPress ENTER to continue.")

            case 5:
                system(self.clear_command)
                expired = self.warehouse.get_expired_items()
                if expired:
                    print_report(expired)
                else:
                    print("No expired items.")
                input("\nPress ENTER to continue.")

            case 6:
                system(self.clear_command)
                name = input("Search item: ")
                result = self.warehouse.search_item(name)
                print_report([result]) if result else print("Item not found.")
                input("\nPress ENTER to continue.")

            case 7:
                system(self.clear_command)
                sorted_items = self.warehouse.get_sorted_items(sort_key=self.sort_keys["expiration_date"])
                print_report(sorted_items)
                input("\nPress ENTER to continue.")

            case 8:
                system(self.clear_command)
                sorted_items = self.warehouse.get_sorted_items(sort_key=self.sort_keys["price"])
                print_report(sorted_items)
                input("\nPress ENTER to continue.")

            case 9:
                system(self.clear_command)
                sorted_items = self.warehouse.get_sorted_items(sort_key=self.sort_keys["quantity"])
                print_report(sorted_items)
                input("\nPress ENTER to continue.")

            case 0:
                system(self.clear_command)
                print("Exiting...")
                self.running = False

            case _:
                input("\nInvalid input! Press ENTER to try again.")


if __name__ == "__main__":
    from config import WAREHOUSE_FILE, CLEAR_COMMAND, SORT_KEYS
    from domain.models import Warehouse
    from repositories.csv_repository import ItemRepository
    

    # Setup for standalone use
    repository = ItemRepository(WAREHOUSE_FILE)
    warehouse = Warehouse()
    warehouse.items = repository.load_all()
    manager = MenuManager(warehouse, repository, SORT_KEYS, clear_command=CLEAR_COMMAND)

    while manager.running:
        manager.print_menu()
        manager.get_choice()
        manager.run_choice()
