# 1920 crumpets per day
# only 92% completed
# Crumpets sell in packs of 6

# full number of packages you can sell per day
full_packs = 1920 // 6
# number of crumpets left over
left_over = 1920 % 6
# number of crumpets that are not completed
not_completed = 1920 * 0.08

print(f"Full packs of crumpets: {full_packs}")
print(f"Left over crumpets: {left_over}")
print(f"Crumpets not completed: {not_completed}")