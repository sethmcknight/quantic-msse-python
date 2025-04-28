## list with drink orders
drink_orders = ["espresso", "latte", "cortado", "espresso", "cortado"]
print(f"Drink orders: {drink_orders}")

## number of drink orders
number_of_drink_orders = len(drink_orders)
print(f"There are {number_of_drink_orders} total drink orders")

## number of each drink ordered
espressos_ordered = drink_orders.count("espresso")
lattes_ordered = drink_orders.count("latte")
cortados_ordered = drink_orders.count("cortado")
print(f"{espressos_ordered} of the orders were espresso.")
print(f"{lattes_ordered} of the orders were lattes.")
print(f"{cortados_ordered} of the orders were cortados.")

## scratch the latte, I want a cactus water
drink_orders[1] = "cactus water"
print(f"Updated drink orders: {drink_orders}")

## save and modify the list for tomorrow
tomorrow_drink_orders = drink_orders.copy()
tomorrow_drink_orders.remove("cactus water")
print(f"Tomorrow's drink orders: {tomorrow_drink_orders}")
print(f"Today's drink orders: {drink_orders}")