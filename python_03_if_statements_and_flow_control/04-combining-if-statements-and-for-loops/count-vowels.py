# This program demonstrates how to get user input
# and use a for loop with an if statement to 
# count the number of vowels in the input message.

while True:
    # Get user input
    message = input("Enter a message to count the vowels.\nType 'exit' to quit.\n-Message: ")

    # Check if the user wants to exit
    if message.lower() == 'exit':
        print("Goodbye!")
        break

    # Initialize a counter for vowels
    vowel_count = 0

    # Loop through each character in the message and check if it's a vowel
    # If it is, increment the counter
    for character in message:
        if character.lower() in "aeiou":
            vowel_count += 1

    # Print the total number of vowels found
    print(f"There are {vowel_count} vowels in the message: {message}")