Python E-Commerce System (Object Oriented Programming)

1. Project Overview
This project is a text-based shopping cart simulator designed to demonstrate Object-Oriented Programming (OOP) principles in Python.
The system handles a product catalog with different logic for physical and digital goods.

2. Key Features

a. Dynamic Pricing: Automatically calculates costs based on item type—adding shipping for physical goods or applying bulk discounts for digital ones.
b. Inventory Management: Uses a Python Dictionary for O(1) fast lookups of products by ID.
c. Robust Input Handling: Prevents system crashes during user interaction by using try/except blocks for data validation.
d. Unit Tested: Includes a unittest suite to verify shipping and discount logic.

3. OOP Architecture

The system is built on a hierarchical structure to ensure code reusability:

a. Inheritance: A base Product class defines core attributes, while PhysicalProduct and DigitalProduct serve as child classes. 
b. Polymorphism: The get_price(quantity) method is overridden in child classes to handle specific business logic:
  b.a Physical: Adds a shipping_cost * quantity to the total.
  b.b Digital: Applies a 10% discount if the quantity is 5 or more.

4. Quality Assurance

The project includes a test suite (unit_test.py) that validates:

a. Correct shipping calculations for physical items.
b. Accurate 10% discount application for bulk digital purchases.

5. How to Run
(Prerequisites)
a. Ensure you have Python 3.6 or higher installed.
b. Keep source_code.py and unit_test.py in the same directory.
(Main Application)
a. Run the application: python source_code.py.
b. To run tests: python unit_test.py.

6. Credits

Anirudh Gopishankar 
Yohan Amaratunga
