mins = 0
temp = 110

while temp >= 30:
    mins += 1
    temp *= 0.98
    print(f"Minute {mins}: {temp:.2f} degrees Celsius")