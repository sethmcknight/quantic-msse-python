prompt = "Enter the radius of a circle (use '0' to exit): "

while True:
    try:
        radius = float(input(prompt))
        if radius == 0:
            print("Exiting the program.")
            break
        elif radius < 0:
            print("Invalid input. Please enter a positive number.")
            continue
        else:
            area = 3.14 * radius ** 2
            print(f"The area of the circle with radius {radius} is: {area}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")