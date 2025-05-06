order_cost = 123.45

if order_cost >=50:
    shipping_cost = 0
    print("Free shipping!")
else:
    shipping_cost = (order_cost * 0.10)
    print(f"Shipping cost: ${shipping_cost:.2f}")

total_cost = order_cost + shipping_cost
print(f"Total cost: ${total_cost:.2f}")