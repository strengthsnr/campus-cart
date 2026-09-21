"""
CampusCart - Stage 2
A simpe command-line shopping application.
"""

# CampusCart manages products, shopping carts, stock and checkout.

#Creation of inventory dictionary with product details including name, price, and stock quantity.
inventory = {
    "101": {
        "name": "Notebook",
        "price": 2.50,
        "stock": 15
    },
    "102": {
        "name": "Pen",
        "price": 1.50,
        "stock": 20
    },
    "103": {
        "name": "Pencil",
        "price": 1.00,
        "stock": 30
    },
    "104": {
        "name": "Eraser",
        "price": 0.50,
        "stock": 25
    }
}

# Creation of the shopping cart.

cart = []


# Main menu
while True:
    print("\n===== CampusCart Menu =====")
    print("1. View Catalog")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

 