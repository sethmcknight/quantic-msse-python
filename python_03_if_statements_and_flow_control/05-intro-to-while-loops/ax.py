items = ["ax", "adz", "awl", "ax", "ax", "awl"]
print(items)

while "ax" in items:
    items.remove("ax")
    print(items)
print("No more axes.")