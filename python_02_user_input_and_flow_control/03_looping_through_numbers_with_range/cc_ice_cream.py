# Welcome customer to the ice cream shop
print("Welcome to the Ice Cream Shop!")
# Ask the custome for three flavors they want
flavors = []
for i in range(3):
    flavor = input("Enter a flavor you want: ")
    flavors.append(flavor)
# Print the flavors
print(f"Here's your flavors: {flavors}\nEnjoy your ice cream!")
