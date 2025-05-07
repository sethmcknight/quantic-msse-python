rates = [17, 21, 180, 24]

converted_rates = []

for rate in rates:
    if rate >= 15 and rate <= 25:
        converted_rates.append(rate * 4)
    else:
        converted_rates.append("NA")
    
print(converted_rates)