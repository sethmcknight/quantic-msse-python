temps = [65, 32, 50, -2, 78, 33, 57, 90, 100, 45, -10, 0, 25, 80, 60, 70, 85, 95, 55, 40, 75, 88, 92, 68, 72, 82, 84, 98, 99, 101]

for i in range(len(temps)):
    temps[i] = round((temps[i] - 32) / 1.8, 1)

print(temps)

humidities = [87, 56, 80, 80, 37]

for i in range(len(humidities)):
    print(humidities[i])