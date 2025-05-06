systolic = int(input("Enter your systolic blood pressure reading: "))
diastolic = int(input("Enter your diastolic blood pressure reading: "))
# Check if the blood pressure reading is in the normal range
if systolic < 90 or diastolic < 60:
    print("You have low blood pressure.")
elif systolic < 120 or diastolic < 80:
    print("Your blood pressure is normal.")
elif systolic < 140 or diastolic < 90:
    print("You have prehypertension.")
elif systolic < 190 or diastolic < 100:
    print("You have high blood pressure.")
else:
    print("Invalid reading, try again.")
