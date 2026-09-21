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

    choice = input("Enter your choice (1-5): ").strip().lower()

    if choice == "1":
        print("\n===== CampusCart Catalog =====")
        for item_id, item in inventory.items():
            print(
                item_id,
                "-",
                item["name"],
                "| Price:",
                item["price"],
                "| Stock:",
                item["stock"]
            )
    elif choice == "2":
        item_id = input("Enter the product ID to add to cart: ").strip()
        if item_id not in inventory:
            print("Product not found. Please try again.")
            continue
        quantity_input = input("Enter the quantity: ").strip()
        try:
            quantity = int(quantity_input)
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")
            continue
        if quantity <= 0:
            print("Quantity must be greater than zero. Please try again.")
            continue
        if quantity > inventory[item_id]["stock"]:
            print("Not enough stock available. Please try again.")
            continue
        price = inventory [item_id]["price"]
        subtotal = price * quantity
        cart_item = {
            "id": item_id,
            "name": inventory[item_id]["name"],
            "price": price,
            "qty": quantity,
            "subtotal": subtotal
        }
        cart.append(cart_item)
        print("Item added to cart.")
        cart_quantity = 0

        for item in cart:
            cart_quantity += item["qty"]
        if cart_quantity + quantity > inventory[item_id]["stock"]:
            print("Not enough stock available. Please try again.")
            continue
    elif choice == "3":
        if not cart:
            print("Your cart is empty")
            continue
        print("\n===== Your cart =====")
        cart_total = 0
        for item in cart:
            print (
                item["name"],
                "x",
                item["qty"],
                "|",
                item["subtotal"]
            )
            cart_total += item["subtotal"]
        print("Total:", cart_total)
    elif choice == "4":
        if not cart:
            print("Your cart is empty")
            continue
        cart_total = 0
        for item in cart:
            cart_total += item["subtotal"]
        discount = 0
        if cart_total > 50:
            discount = cart_total * 0.10
        final_total = cart_total - discount
        for item in cart:
            inventory[item["id"]]["stock"] -= item["qty"]
        print("\n===== RECEIPT =====")
        for item in cart:
            print(
                item["name"],
                "x",
                item["qty"],
                "|",
                item["subtotal"]
            )

        print("____________________________")
        print("Subtotal:", cart_total)
        print("Discount:", discount)
        print("Total:", final_total)
        print("============================")
        print("Thank you for shopping with CampusCart!")

        cart.clear()