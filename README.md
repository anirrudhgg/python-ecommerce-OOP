# Python E-Commerce System (OOP)

A text-based shopping cart that demonstrates object-oriented design in Python: a product hierarchy with different pricing rules for physical and digital goods, business logic kept separate from the console interface, and a unit test suite.

## Features

- **Inheritance and polymorphism:** `PhysicalProduct` and `DigitalProduct` extend `Product` and override `get_price()`:
  - physical goods add a shipping cost per item
  - digital goods get a 10% bulk discount from 5 items
- **Exact money arithmetic:** prices use `Decimal` and are rounded to whole cents, so totals never show float errors like `0.30000000000000004`
- **O(1) product lookup:** the inventory is a dictionary keyed by product ID
- **Testable design:** `add_item()` and `cart_total()` contain the logic and raise `ValueError` for invalid input; the console methods only handle input and output
- **Input validation:** unknown IDs, zero or negative quantities and non-numeric input are rejected without crashing

## Class design

```
Product (product_id, name, price)
├── get_price(quantity)      price × quantity
├── PhysicalProduct (+ weight_kg, shipping_cost)
│   └── get_price(quantity)  + shipping × quantity
└── DigitalProduct (+ file_size_mb)
    └── get_price(quantity)  − 10% if quantity ≥ 5

StoreApp
├── inventory: dict[str, Product]
├── cart: list[(Product, quantity)]
├── add_item(), cart_total()               business logic
└── show_catalog(), add_to_cart(), checkout(), run()   console interface
```

A UML diagram and the full documentation are in `Documentation/`.

## Getting started

Requires Python 3.8+ and no extra packages. From the repository root:

```
python src/store.py                    # start the store
python -m unittest discover tests -v   # run the tests
```

Menu options: `1` view catalog, `2` add an item (product ID, then quantity), `3` checkout, `4` exit.

## Tests

`tests/test_store.py` has 12 tests covering:

- base price, shipping per item, and the discount just below and at the 5-item threshold
- rounding to cents and the absence of float errors
- the total of a mixed cart, and an empty cart
- rejection of unknown IDs, zero and negative quantities, and text entered as a quantity (simulated with `unittest.mock`)
- the cart being cleared after checkout

## Project structure

```
├── src/store.py            Product classes and the store application
├── tests/test_store.py     Unit tests
└── Documentation/          UML diagram and project documentation
```

## Team

- Anirudh Gopishankar
- Yohan Amaratunga
