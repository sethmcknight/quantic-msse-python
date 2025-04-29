# create unique id's for each cactus of 500
cactus_ids = []

for i in range(1, 501):
    id = f"cactus{i}"
    cactus_ids.append(id)

# Print the cactus ids
print(f'The cactus ids are: {cactus_ids}')