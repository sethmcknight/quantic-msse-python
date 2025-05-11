initial_deposit = 10
current_balance = initial_deposit
interest_rate = 0.10
next_report = 100
years = 0

while current_balance < 1000:
    years += 1
    current_balance *= (1 + interest_rate)
    if current_balance > next_report:
        next_report += 100
        print(f"Year {years}: Current balance is ${current_balance:.2f}")
        continue

print(f"{years} Years for ${initial_deposit} to grow to ${current_balance:.2f} at {interest_rate:.0%} interest.")