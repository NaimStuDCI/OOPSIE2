from datetime import date, datetime

class Item:
    def __init__(self, name, quantity=0, expiration_date="1970-01-01", price=0.0):
        self.name = name
        self.quantity = int(quantity)
        self.expiration_date = expiration_date
        self.price = float(price)

    def is_expired(self, today=None):
        today = today or date.today()
        return datetime.strptime(self.expiration_date, "%Y-%m-%d").date() < today

    def update(self, quantity=None, expiration_date=None, price=None):
        if quantity is not None: self.quantity = int(quantity)
        if expiration_date is not None: self.expiration_date = expiration_date
        if price is not None: self.price = float(price)

class Warehouse:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        if any(existing.name == item.name for existing in self.items):
            raise ValueError("Item already exists")
        self.items.append(item)

    def remove_item(self, name: str):
        self.items = [item for item in self.items if item.name != name]

    def update_item(self, name: str, updates: dict):
        for item in self.items:
            if item.name == name:
                item.update(**updates)
                return
        raise ValueError("Item not found")

    def get_expired_items(self):
        return [item for item in self.items if item.is_expired()]

    def search_item(self, name: str):
        return next((item for item in self.items if item.name == name), None)

    def get_sorted_items(self, key: str):
        if key == "quantity":
            return sorted(self.items, key=lambda x: x.quantity)
        elif key == "expiration_date":
            return sorted(self.items, key=lambda x: datetime.strptime(x.expiration_date, "%Y-%m-%d"))
        elif key == "price":
            return sorted(self.items, key=lambda x: x.price)
        else:
            return self.items

    def get_occupancy(self):
        return len(self.items)
