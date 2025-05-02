# Number lists
numbers = (1, 2, 3, 4, 5)
squares = []  
cubes = []
quarts = []
quints = []
# String lists of numbers
numbers_string = []
squares_string = []
cubes_string = []
quarts_string = []
quints_string = []
# Populates a list of the numbers in the numbers tuple
for number in numbers:
    numbers_string.append(str(number))
# Populates a list of the squares of each number in the numbers tuple
for number in numbers:
    number **= 2
    squares.append(number)  
    squares_string.append(str(number))
# Populates a list of the cubes of each number in the numbers tuple
for number in numbers:
    number **= 3
    cubes.append(number)  
    cubes_string.append(str(number))
# Populates a list of the quartics of each number in the numbers tuple
for number in numbers:
    number **= 4
    quarts.append(number)  
    quarts_string.append(str(number))   
# Populates a list of the quintics of each number in the numbers tuple
for number in numbers:
    number **= 5
    quints.append(number)  
    quints_string.append(str(number))  

# Prints the numbers, squares, cubes, quartics, and quintics of each number in the numbers tuple
print(f"Numbers: " + " * ".join(numbers_string) + f" = {eval('*'.join(numbers_string))}")
print(f"Squares: " + " * ".join(squares_string) + f" = {eval('*'.join(squares_string))}")
print(f"Cubes: " + " * ".join(cubes_string) + f" = {eval('*'.join(cubes_string))}")
print(f"Quartics: " + " * ".join(quarts_string) + f" = {eval('*'.join(quarts_string))}")
print(f"Quintics: " + " * ".join(quints_string) + f" = {eval('*'.join(quints_string))}")
