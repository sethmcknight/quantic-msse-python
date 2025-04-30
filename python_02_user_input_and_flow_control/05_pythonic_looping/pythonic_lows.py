# This is a simple temperature conversion program that converts a list of Fahrenheit temperatures to Celsius & Kelvin.
# It uses a for loop to iterate through each temperature in the fahrenheit_temps list, applies the conversion formula, rounds the result to one decimal place, and appends it to the celcius_temps list. Finally, it prints the list of Celsius temperatures.
fahrenheit_temps = [65, 32, 50, -2]
celcius_temps = []
kelvin_temps = []
# Print the Fahrenheit temperatures
print(f"The Fahrenheit temperatures are: {fahrenheit_temps}")
# Convert Fahrenheit to Celsius
# Formula: C = (F - 32) / 1.8
for temp in fahrenheit_temps:
    temp = (temp-32) / 1.8
    temp = (round(temp,1))
    celcius_temps.append(temp)
print(f"The Celsius temperatures are: {celcius_temps}")
# Convert Celsius to Kelvin
# Formula: K = C + 273.15
for temp in celcius_temps:
    temp = temp + 273.15
    temp = (round(temp,1))
    kelvin_temps.append(temp)
print(f"The Kelvin temperatures are: {kelvin_temps}")