# Warehouse Inventory Manager - OOPSIE 2.0

A modular Python application for managing warehouse inventory with flexible storage backends (CSV/JSON), robust input validation, and comprehensive automated tests.

## Features

- **Add, remove, update, search, and sort inventory items**
- **Support for CSV and JSON storage backends** (select via config only)
- **Expiry tracking** for perishable/limited-time goods
- **Simple terminal-based menu interface**
- **Input validation** with user guidance
- **Modular domain and repository design** (easy to extend/maintain)
- **Automated unit tests** for core logic and I/O


## Directory Structure

```
.
├── config.py
├── data/
│   ├── warehouse_inventory.csv
│   └── warehouse_inventory.json
├── domain/
│   └── models.py
├── helpers.py
├── main.py
├── menu.py
├── repositories/
│   ├── abstract_repository.py
│   ├── csv_repository.py
│   ├── json_repository.py
│   └── __init__.py
├── tests/
│   ├── test_csv_repository.py
│   ├── test_helpers.py
│   └── test_models.py
```


## Requirements

- **Python 3.8+** recommended
- No external packages (pure standard library)


## Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/warehouse-inventory-manager.git
cd warehouse-inventory-manager
```

2. **Configure storage backend:**
    - Open `config.py`.
    - Set `WAREHOUSE_FILE` to either the CSV or JSON inventory file in the `data/` directory (default is CSV).
3. **Run the application:**

```bash
python main.py
```

Or directly via the menu:

```bash
python menu.py
```

4. **Follow prompts in the terminal menu** to add, update, or manage items.

## Usage

- **Add Item**: Enter unique name, quantity, price, and expiration date (YYYY-MM-DD).
- **Remove/Search/Update**: Input the item name as prompted.
- **Sort/Report**: Sort by price, quantity, or expiration date for actionable inventory overview.
- **Expired Item Check**: Instantly lists all expired items.

> All user data is validated on input for integrity and safety.

## Testing

All core logic and repositories are covered with unit tests using `unittest` and mocks for I/O.

To run the tests:

```bash
python -m unittest discover tests
```


## Design Notes

- **Repository Pattern** for data access — easily swap CSV/JSON without changing business logic.
- **Menu and helpers** are decoupled for straightforward testability and future interface upgrades.
- **Testable from input to storage:** Includes test cases for input helpers, item mutation, persistence, and reporting.


## Future Enhancements

- Richer item categories/entities
- Enhanced terminal or GUI user interface
- Continuous Integration (CI) pipeline
- Improved user authentication and versioning audit (see OOPSIE 2.0 presentation)
- API or web frontend


## Maintainers

Ekaterina Nestoklon, Christoph Schneider \& Naim Burrack

**Q\&A / Contributions:**
PRs and issues are welcome for new features, bugfixes, or improvements!

If you need custom badges or additional project metadata, let me know!

<div style="text-align: center">⁂</div>

[^1]: models.py

[^2]: config.py

[^3]: menu.py

[^4]: OOPSIE-2.0-PRESENTATION-REFACTORIZED.pdf

[^5]: warehouse_inventory.json

[^6]: warehouse_inventory.csv

[^7]: helpers.py

[^8]: test_helpers.py

[^9]: test_csv_repository.py

