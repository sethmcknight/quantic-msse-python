vin = "1HGBH41JX8MN109186"

# Use indexing to extract information from the VIN:
country_code = vin[0]
manufacturer_code = vin[1:3]
vehicle_portrait = vin[3:8]
vin_check_digit = vin[8]
model_year = vin[9]
assembly_plant = vin[10]
vehicle_serial_number = vin[11:]

# Use f-strings to format and print the extracted information:
print(f"Country Code: {country_code}")
print(f"Manufacturer Code: {manufacturer_code}")
print(f"Vehicle Portrait: {vehicle_portrait}")
print(f"VIN Check Digit: {vin_check_digit}")
print(f"Model Year: {model_year}")
print(f"Assembly Plant: {assembly_plant}")
print(f"Vehicle Serial Number: {vehicle_serial_number}")
# Use slicing to extract the last 4 characters of the VIN and print using an f-string:
print(f"Last 4 characters of VIN: {vin[-4:]}")
