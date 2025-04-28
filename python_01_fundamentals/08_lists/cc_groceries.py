cart_items = ["milk", "eggs", "flour", "butter"]
print(f"Items in your cart: {cart_items}")
cart_items[0] = "chocolate"
print(f"Items in your cart: {cart_items}")
cart_items.remove("eggs")
cart_items.remove("flour")
print(f"Items in your cart: {cart_items}")
for item in cart_items[:]:
    print(f"Okay, we've packed your {cart_items.pop()}!")
print(f"Items in your cart: {cart_items}")