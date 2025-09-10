# Loan Calculator

A Python function to calculate loan balances after payments using `itertools.accumulate`.

## Usage

```python
from loan_calculator import calculate_loan_balances, calculate_loan_balances_annual

# Monthly compounding (default) - $2000 loan at 4% annual interest
balances = calculate_loan_balances(2000, 0.04, [100, 200, 150])
print(balances)  # [1906.67, 1713.03, 1568.74]

# Annual compounding (like your elegant solution)
balances = calculate_loan_balances_annual(2000, 0.04, [100, 200, 150])
print(balances)  # [2000, 1980, 1859, 1783]

# Custom compounding periods (quarterly = 4 periods/year)
balances = calculate_loan_balances(2000, 0.04, [100, 200, 150], compounding_periods=4)
```

## Functions

- `calculate_loan_balances(principal, annual_rate, payments, compounding_periods=12)` - Flexible compounding periods
- `calculate_loan_balances_annual(principal, annual_rate, payments)` - Simple annual compounding (includes initial balance)
- `print_payment_schedule(principal, annual_rate, payments, compounding_periods=12)` - Detailed payment breakdown

## Key Features

- **Uses `itertools.accumulate`** for elegant functional programming approach
- **Flexible compounding periods** (monthly, quarterly, annual, etc.)
- **Annual compounding convenience function** matching your original elegant solution
- **Detailed payment schedules** showing interest vs. principal breakdown

## Example

Run `python3 loan_calculator.py` to see examples with both monthly and annual compounding.
