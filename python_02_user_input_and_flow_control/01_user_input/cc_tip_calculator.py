name = input("Enter your name: ")
total_bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage you want to give: "))
# Calculate the tip amount
tip_amount = (tip_percentage / 100) * total_bill
# Calculate the total amount to be paid
total_amount = total_bill + tip_amount
# Print the results
print(f"Hello, {name}!")
print(f"The tip amount is: ${tip_amount:.2f}")
print(f"The total amount to be paid is: ${total_amount:.2f}")