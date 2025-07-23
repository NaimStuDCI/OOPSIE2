import csv
from domain.models import Item

class ItemRepository:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_all(self):
        items = []
        with open(self.filepath, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                items.append(Item(
                    name=row["item"],
                    quantity=int(row["quantity"]),
                    expiration_date=row["expiration_date"],
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
                    "expiration_date": item.expiration_date,
                    "price": item.price
                })
