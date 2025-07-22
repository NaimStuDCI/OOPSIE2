import csv
from domain.models import Item

def load_items(filepath):
    items = []
    with open(filepath, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(Item(
                name=row["item"],
                quantity=row["quantity"],
                expiration_date=row["expiration_date"],
                price=row["price"]
            ))
    return items

def save_items(filepath, items):
    with open(filepath, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["item", "quantity", "expiration_date", "price"])
        writer.writeheader()
        for item in items:
            writer.writerow({
                "item": item.name,
                "quantity": item.quantity,
                "expiration_date": item.expiration_date,
                "price": item.price
            })
