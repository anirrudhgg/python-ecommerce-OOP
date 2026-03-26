Python E-Commerce System (Object Oriented Programming)

1. Project Overview
This project is a text-based shopping cart simulator designed to demonstrate Object-Oriented Programming (OOP) principles in Python.
The system handles a product catalog with different logic for physical and digital goods.

2. Key Features

2.1 Dynamic Pricing: Automatically calculates costs based on item type—adding shipping for physical goods or applying bulk discounts for digital ones.
2.2 Inventory Management: Uses a Python Dictionary for O(1) fast lookups of products by ID.
2.3 Robust Input Handling: Prevents system crashes during user interaction by using try/except blocks for data validation.
2.4 Unit Tested: Includes a unittest suite to verify shipping and discount logic.

3. OOP Architecture

The system is built on a hierarchical structure to ensure code reusability:

3.1 Inheritance: A base Product class defines core attributes, while PhysicalProduct and DigitalProduct serve as child classes. 
3.2 Polymorphism: The get_price(quantity) method is overridden in child classes to handle specific business logic:
  3.2.1 Physical: Adds a shipping_cost * quantity to the total.
  3.2.2 Digital: Applies a 10% discount if the quantity is 5 or more.

4. Quality Assurance

The project includes a test suite (unit_test.py) that validates:

4.1 Correct shipping calculations for physical items.
4.2 Accurate 10% discount application for bulk digital purchases.

5. How to Run
(Prerequisites)
5.1 Ensure you have Python 3.6 or higher installed.
5.2 Keep source_code.py and unit_test.py in the same directory.
(Main Application)
5.3 Run the application: python source_code.py.
5.4 To run tests: python unit_test.py.

6. Credits

Anirudh Gopishankar 
Yohan Amaratunga
