rates = [0.07, 0.04, 0.12, 0.06, 0.08]
balance = 1000

print("savings account balances")
for rate in rates:
    balance *= 1 + rate
    print(f"${balance:.2f}")

print("car loan payments")
payments = [250, 250, 185]
total = 0
for payment in payments:
    total += payment
    print(f"${total:.2f}")