age = int(input("Your age: "))
driver_license = input("Do you have a driver's license? (yes/no): ")
# Check if the user is eligible for a rental car based on age and driver's license
if age >= 25 and driver_license == "yes":
    print("No restrictions.")
elif age >= 21 and driver_license == "yes":
    print("Add insurance.")
elif age >= 18 and driver_license == "yes":     
    print("Co-signer needed.")
elif age >= 16:
    print("Bike rental allowed.")
else:
    print("Conditions not met.")


