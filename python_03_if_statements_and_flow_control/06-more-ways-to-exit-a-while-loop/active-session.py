active = True

while active:
    reply = input("Still working? (y/n): ")

    if reply == "n":
        print("Ending session.")
        active = False
    elif reply == "y":
        print("Keeping session active.")

print("Session ended.")