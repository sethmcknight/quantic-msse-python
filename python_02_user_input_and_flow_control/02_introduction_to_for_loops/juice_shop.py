flavors = ["beet", "green", "mango"]
boosters = ["wheatgrass", "probiotics"]
seeds = ["chia", "flax"]
sizes = ["small", "medium", "large"]
types = ["cup", "bottle", "jug"]
orders = ["A62", "A63", "A64"]

for flavor in flavors:
    print(f"We have {flavor} juice!")
    print("Yum!\n")
print("Which would you like?\n")

for booster in boosters:
    print(f"Add {booster}?\n")

for seed in seeds:
    print(f"Add {seed} seeds?")
    print("They're good for you!\n")
print("Seeds are healthy!\n")

for size in sizes:
    print(f"You can get a {size}.")
print("That size is great!\n")

print("We have the following containers:")
for t in types:
    print(f"- {t}")
print("\n")

for order in orders:
    print(f"Order {order} is complete!\n")
    print("Thank you!\n")
