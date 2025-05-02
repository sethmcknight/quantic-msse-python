trail = input("Which trail are you taking? ")
length = float(input("How long is the trail in Kilometers? "))
while True:
	days = int(input("How many days do you plan to hike? "))
	if days > 0:
		break
	print("Number of days must be greater than 0. Please try again.")
daily_distance = round(length / days, ndigits=1)
print(f"You will hike {daily_distance} kilometers each day on the {trail} trail.")