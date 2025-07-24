import csv
from datetime import datetime
from domain.models import Item
from repositories.abstract_repository import AbstractItemRepository

class ItemRepository(AbstractItemRepository):
    def __init__(self, filepath):
        self.filepath = filepath + ".csv"

    def load_all(self):
        items = []
        with open(self.filepath, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                expiration_date = datetime.strptime(row["expiration_date"], "%Y-%m-%d").date()
                items.append(Item(
                    name=row["item"],
                    quantity=int(row["quantity"]),
                    expiration_date=expiration_date,
                    price=float(row["price"])
                ))
        return items

    def save_all(self, items):
        with open(self.filepath, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["item", "quantity", "expiration_date", "price"])
            writer.writeheader()
            for item in items:
                writer.writerow({
                    "item": item.name,
                    "quantity": item.quantity,
                    "expiration_date": item.expiration_date.strftime("%Y-%m-%d"),
                    "price": item.price
                })
