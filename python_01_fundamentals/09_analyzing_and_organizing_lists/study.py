# Summary of Study Data
## list of patients by last name
patients = ["davis", "lee", "jones", "bell", "garcia"]
print(f"Patients Alphabetical: {sorted(patients)}")
print(f"First subject: \n{sorted(patients)[0].title()}")

## study parameters as a tuple with dosage, frequency, and form
parameters = (300, "daily", "chewable")
## tuples are immutable so with throw a TypeError if we try to reassign - parameters[0] = 400

## list with study results from day 1
outcomes = ["s", "h", "h", "s", "h"]

## identify the number of patients in the study
num_people = len(outcomes)
print(f"There are {num_people} patients in the study.")

## identify the number of patients who are still sick
num_sick = outcomes.count("s")
print(f"Day 1: {num_sick} patients are still sick.")

## archive day 1 results
outcomes_old = outcomes.copy()
num_sick_old = num_sick

## update outcomes with day 1 results
outcomes[3] = "h"
num_sick = outcomes.count("s")
print(f"Day 2: {num_sick} patients are still sick.")

## compare day 1 and day 2 results
print(f"Yesterday's results: {outcomes_old}")
print(f"Today's results: {outcomes}")
