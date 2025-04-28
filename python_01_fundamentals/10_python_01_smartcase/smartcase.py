user = ("  ray ", " li", 27, 40.5)

# Print welcome statement
first_name = user[0].strip().title()
print(f"Hi {first_name}!\nThanks for joining!")

# convert height to feet and inches | height, feet, inches
height = 70
feet = int(height // 12)
inches = int(height % 12)
print("Inches: " + str(height))
# print in centimeters
print(f"That's {height * 2.54} cm tall.")
print(f"Your height is {feet} feet and {inches} inches.")

request = "2 green and 1 red"
first_amount = int(request[0])
second_amount = int(request[-5])

sizes = ("S", "M", "L")
fabrics = ["cotton", "wool"]
style = "vintage"

orders = ['hat', 'hoodie', 'jeans', 'dress', 't-shirt', 'dress']
print(len(orders))
print(orders.count("dress"))
orders.remove("dress")
print(orders)
prin("button")