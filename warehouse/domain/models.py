from datetime import date


class Item:
    def __init__(self, name, quantity=0, expiration_date=date(1970, 1, 1), price=0.0):
        self.name = name
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.price = price

    def is_expired(self, today=None):
        today = today or date.today()
        return self.expiration_date < today

    def update(self, quantity=None, expiration_date=None, price=None):
        if quantity is not None:
            self.quantity = quantity
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if price is not None:
            self.price = price


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

    def get_sorted_items(self, sort_key=None):
        if sort_key is None:
            return self.items
        return sorted(self.items, key=sort_key)

    def get_occupancy(self):
        return len(self.items)
