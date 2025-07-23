import re
from domain.models import Item
from datetime import datetime

def input_item(existing_names):
    while True: # Validate item name – must be unique, only letters/spaces
        name = input("Item name: ").strip()
        if not name:
            print("Name cannot be empty.")
        elif not re.match(r"^[A-Za-z ]+$", name):
            print("Name can only contain letters and spaces.")
        elif name in existing_names:
            print("An item with this name already exists.")
        else:
            break
    while True: # Quantity validation
        quantity_input = input("Quantity: ").strip()
        if not quantity_input.isdigit():
            print("Quantity must be a whole number.")
        else:
            quantity = int(quantity_input)
            break
    while True: # Price validation
        price_input = input("Price (e.g., 19.99): ").strip()
        try:
            price = float(price_input)
            if price < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive price like 12.50.")
    while True: # Expiration date validation
        date_str = input("Expiration Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d").date()
            expiration_date = date_str
            break
        except ValueError:
            print("Invalid format. Please enter date as YYYY-MM-DD.")

    return Item(name=name, quantity=quantity, expiration_date=expiration_date, price=price)

def print_report(items):
    print(f"\n{'Item':<20} {'Quantity':<10} {'Expiration Date':<20} {'Price':<10}")
    for item in items:
        try:
            formatted_date = item.expiration_date.strftime("%Y-%m-%d")
        except AttributeError:
            formatted_date = str(item.expiration_date)
        print(f"{item.name:<20} {item.quantity:<10} {formatted_date:<20} {item.price:<10.2f}")
