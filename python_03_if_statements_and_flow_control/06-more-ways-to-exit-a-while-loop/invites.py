print("Tell us who to invite!")
print("Type 'quit' when done")

invitees = []
name = ""

while True:
    name = input("Invitee:")

    if name.lower() == 'quit':
        print("Done!")
        break

    invitees.append(name.title())

print(f"Invitees: {invitees}")