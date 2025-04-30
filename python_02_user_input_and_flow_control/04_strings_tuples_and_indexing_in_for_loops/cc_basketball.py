# Challenge 1
my_string = "NBA"
# Print each character in the string in lowercase
for character in my_string:
    print(character.lower())

# Challenge 2
nba_player_weights = [190, 185, 250, 190]
nba_player_weights_kg = []
# convert the weights of NBA Players from pounds to kilograms
for i in range(len(nba_player_weights)):
    player_weight_kg = round(nba_player_weights[i] * 0.45, 2)
    nba_player_weights_kg.append(player_weight_kg)
# Print the converted weights of NBA Players in kilograms
print(nba_player_weights_kg)

# Challenge 3
nba_player_heights = [1.98, 1.75, 2.03, 1.91]
nba_player_bmis = []
# Calculate the BMI of NBA Players using the formula: weight (kg) / height (m)^2
for i in range(len(nba_player_heights)):
    bmi = round(nba_player_weights_kg[i] / (nba_player_heights[i] ** 2), 2)
    nba_player_bmis.append(bmi)
# Print the calculated BMI of NBA Players
print(nba_player_bmis)