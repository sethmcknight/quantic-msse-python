first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
adult_tickets = int(input("How many adult tickets do you want? "))
kid_tickets = int(input("How many tickets do you want for kids under 12? "))
adult_ticket_price = 17.00
kid_ticket_price = 14.00
total_tickets = adult_tickets + kid_tickets
total_price = (adult_tickets * adult_ticket_price) + (kid_tickets * kid_ticket_price)
tax_rate = 0.078
total_price_with_tax = total_price * (1 + tax_rate)
print(f"Hello, {first_name} {surname}!")
print(f"You have purchased {total_tickets} tickets.")
print(f"The total price is: ${total_price:.2f}")
print(f"The total price with tax is: ${total_price_with_tax:.2f}")
