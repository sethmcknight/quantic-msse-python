distances = []
for day in range(1, 5):
    distance = float(input(f"How many kilometers did you hike on day {day}? "))
    distances.append(distance)
total_distance = sum(distances)
print(f"You hiked a total of {total_distance} kilometers.")