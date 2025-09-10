import itertools
from loan_calculator import calculate_loan_balances

# Your elegant solution
payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]
update = lambda balance, payment: round(balance * 1.04) - payment
balances_yours = list(itertools.accumulate(payments, update, initial=2_000))

print("Your solution (annual compounding):")
print("Payments:", payments)
print("Balances:", balances_yours)
print()

# My solution (monthly compounding)
balances_mine = [2000] + calculate_loan_balances(2000, 0.04, payments)

print("My solution (monthly compounding):")
print("Payments:", payments)
print("Balances:", balances_mine)
print()

print("Differences:")
for i, (yours, mine) in enumerate(zip(balances_yours, balances_mine)):
    diff = yours - mine
    print(f"Payment {i}: Your: ${yours}, Mine: ${mine:.2f}, Diff: ${diff:.2f}")
