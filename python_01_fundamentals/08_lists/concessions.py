snacks = ["popcorn", "nuggets", "gummis", "nachos"]
snacks[2] = "hot dogs"
snacks[3] = "pizza"
# snacks.remove("gummis")
out_of_stock = snacks.pop(2)
print(f"Sorry, we're out of {out_of_stock}.")
del snacks[0]
print(snacks)

motto = "I love Python!"
motto[3] = "i"