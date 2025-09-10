# Loan Calculator

A Python function to calculate loan balances after payments.

## Usage

```python
from loan_calculator import calculate_loan_balances

# Calculate balances for a $2000 loan at 4% annual interest
balances = calculate_loan_balances(2000, 0.04, [100, 200, 150])
print(balances)  # [1906.67, 1713.02, 1568.73]
```

## Functions

- `calculate_loan_balances(principal, annual_rate, payments)` - Returns list of balances after each payment
- `print_payment_schedule(principal, annual_rate, payments)` - Prints detailed payment breakdown

## Example

Run `python3 loan_calculator.py` to see an example with your loan parameters.
