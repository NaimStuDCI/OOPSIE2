from datetime import datetime
from domain.models import Item
import json

class ItemRepository:
    def __init__(self, filepath):
        self.filepath = filepath + ".json"
    def load_all(self):
        items = []
        with open(self.filepath, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
            for row in data:
                expiration_date = datetime.strptime(row["expiration_date"], "%Y-%m-%d").date()
                items.append(Item(
                    name=row["item"],
                    quantity=int(row["quantity"]),
                    expiration_date=expiration_date,
                    price=float(row["price"])
                ))
        return items
    def save_all(self, items):
        data = []
        for item in items:
            data.append({
                "item": item.name,
                "quantity": item.quantity,
                "expiration_date": item.expiration_date.strftime("%Y-%m-%d"),
                "price": item.price
            })
        with open(self.filepath, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=2, ensure_ascii=False)






