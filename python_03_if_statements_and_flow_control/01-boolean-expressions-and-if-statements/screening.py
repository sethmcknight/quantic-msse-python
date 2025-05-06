level = int(input("LDL level?"))

if level >= 100:
    print("More tests advised.")
else:
    print("Healthy LDL level!")

print("Next: blood pressure.")

print("Relatives with heart disease?")
relatives = input("Answer yes or no: ")

if relatives == "yes":
    print("Risk factor elevated.")
    risk = "elevated"
else:
    print("Okay, great.")
    risk = "low"
    