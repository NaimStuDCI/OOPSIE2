import os

WAREHOUSE_FILE = "warehouse_inventory"

CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"

SORT_KEYS = {
    "price": lambda x: x.price,
    "quantity": lambda x: x.quantity,
    "expiration_date": lambda x: x.expiration_date
}
