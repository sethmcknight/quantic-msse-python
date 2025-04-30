
numbers = (1, 2, 3, 4, 5)
squares = []  
cubes = []
quarts = []
quints = []
# Populates a list of the squares of each number in the numbers tuple
for num in numbers:
    square = num ** 2
    squares.append(square)
# Populates a list of the cubes of each number in the numbers tuple
for num in numbers:
    cube = num ** 3
    cubes.append(cube)
# Populates a list of the quartics of each number in the numbers tuple
for num in numbers:
    quart = num ** 4
    quarts.append(quart)
# Populates a list of the quintics of each number in the numbers tuple
for num in numbers:
    quint = num ** 5
    quints.append(quint)

# Prints the numbers, squares, cubes, quartics, and quintics of each number in the numbers tuple
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Cubes: {cubes}")
print(f"Quartics: {quarts}")
print(f"Quintics: {quints}")