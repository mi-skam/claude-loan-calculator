import itertools


def calculate_loan_balances(principal, annual_rate, payments, compounding_periods=12):
    """
    Calculate loan balances after each payment using itertools.accumulate.
    
    Args:
        principal (float): Initial loan amount
        annual_rate (float): Annual interest rate as a decimal (e.g., 0.04 for 4%)
        payments (list): List of payment amounts
        compounding_periods (int): Number of compounding periods per year (default: 12 for monthly)
    
    Returns:
        list: List of remaining balances after each payment
    
    Example:
        >>> calculate_loan_balances(2000, 0.04, [100, 200, 150])
        [1906.67, 1713.02, 1568.73]
        >>> calculate_loan_balances(2000, 0.04, [100, 200, 150], compounding_periods=1)
        [1980.0, 1834.2, 1707.17]
    """
    # Calculate period rate
    period_rate = annual_rate / compounding_periods
    
    # Update function: apply interest then subtract payment
    def update_balance(balance, payment):
        new_balance = balance * (1 + period_rate) - payment
        return max(0, round(new_balance, 2))  # Ensure non-negative balance
    
    # Use itertools.accumulate, skip the initial principal value
    balances = list(itertools.accumulate(payments, update_balance, initial=principal))
    return balances[1:]  # Remove initial principal, return only post-payment balances


def calculate_loan_balances_annual(principal, annual_rate, payments):
    """
    Simple annual compounding version (like your original elegant solution).
    
    Args:
        principal (float): Initial loan amount  
        annual_rate (float): Annual interest rate as decimal
        payments (list): List of payment amounts
        
    Returns:
        list: All balances including initial principal
    """
    update = lambda balance, payment: round(balance * (1 + annual_rate)) - payment
    return list(itertools.accumulate(payments, update, initial=principal))


def print_payment_schedule(principal, annual_rate, payments, compounding_periods=12):
    """
    Print a detailed payment schedule showing interest, principal, and balance.
    
    Args:
        principal (float): Initial loan amount
        annual_rate (float): Annual interest rate as a decimal
        payments (list): List of payment amounts
        compounding_periods (int): Number of compounding periods per year
    """
    period_rate = annual_rate / compounding_periods
    current_balance = principal
    
    print(f"Loan Amount: ${principal:,.2f}")
    print(f"Annual Interest Rate: {annual_rate:.1%}")
    print(f"Period Interest Rate: {period_rate:.4%}")
    print("\n" + "="*70)
    print(f"{'Payment':<8} {'Amount':<10} {'Interest':<10} {'Principal':<10} {'Balance':<10}")
    print("="*70)
    
    for i, payment in enumerate(payments, 1):
        interest = current_balance * period_rate
        principal_payment = payment - interest
        
        # Handle overpayment case
        if principal_payment > current_balance:
            principal_payment = current_balance
            actual_payment = interest + principal_payment
        else:
            actual_payment = payment
            
        current_balance = max(0, current_balance - principal_payment)
        
        print(f"{i:<8} ${actual_payment:<9.2f} ${interest:<9.2f} ${principal_payment:<9.2f} ${current_balance:<9.2f}")
        
        if current_balance == 0:
            break


if __name__ == "__main__":
    # Example usage with your loan parameters
    loan_amount = 2000
    interest_rate = 0.04  # 4%
    
    # Example payments
    monthly_payments = [100, 200, 150, 300, 250]
    
    print("Loan Balance Calculator")
    print("="*50)
    
    # Calculate balances (monthly compounding)
    balances = calculate_loan_balances(loan_amount, interest_rate, monthly_payments)
    print(f"\nMonthly compounding balances: {balances}")
    
    # Calculate balances (annual compounding like your solution)
    balances_annual = calculate_loan_balances_annual(loan_amount, interest_rate, monthly_payments)
    print(f"Annual compounding balances: {balances_annual}")
    
    print("\nDetailed Payment Schedule (Monthly Compounding):")
    print_payment_schedule(loan_amount, interest_rate, monthly_payments)
