# A program that asks if a user wants ketchup
# and exits the loop if they say "yes" or "no"

invalid_answer = True

while invalid_answer:
    user_input = input("\nDo you want ketchup? (yes/no): \n \n").lower()
    if user_input not in ("yes", "no"):
        print(f"\n{user_input} is an invalid answer.\nPlease answer 'yes' or 'no'.")
    elif user_input == "yes":
        print("\nYay, ketchup!")
        invalid_answer = False
    elif user_input == "no":
        print("\nBoo, no ketchup!")
        invalid_answer = False


print("\nAt least there's mustard!\nThe End.")
