from config import WAREHOUSE_FILE, CLEAR_COMMAND, SORT_KEYS
from domain.models import Warehouse
from menu import MenuManager
from repositories.csv_repository import ItemRepository


def main():
    repository = ItemRepository(WAREHOUSE_FILE)
    warehouse = Warehouse()
    warehouse.items = repository.load_all()
    manager = MenuManager(warehouse, repository, SORT_KEYS, clear_command=CLEAR_COMMAND)

    while manager.running:
        manager.print_menu()
        manager.get_choice()
        manager.run_choice()


if __name__ == "__main__":
    main()
