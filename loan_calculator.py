def calculate_loan_balances(principal, annual_rate, payments):
    """
    Calculate loan balances after each payment.
    
    Args:
        principal (float): Initial loan amount
        annual_rate (float): Annual interest rate as a decimal (e.g., 0.04 for 4%)
        payments (list): List of payment amounts
    
    Returns:
        list: List of remaining balances after each payment
    
    Example:
        >>> calculate_loan_balances(2000, 0.04, [100, 200, 150])
        [1973.33, 1766.82, 1611.69]
    """
    # Convert annual rate to monthly rate
    monthly_rate = annual_rate / 12
    
    balances = []
    current_balance = principal
    
    for payment in payments:
        # Calculate interest for this period
        interest = current_balance * monthly_rate
        
        # Apply payment (payment goes toward interest first, then principal)
        principal_payment = payment - interest
        
        # Update balance
        current_balance = current_balance - principal_payment
        
        # Ensure balance doesn't go negative
        current_balance = max(0, current_balance)
        
        balances.append(round(current_balance, 2))
    
    return balances


def print_payment_schedule(principal, annual_rate, payments):
    """
    Print a detailed payment schedule showing interest, principal, and balance.
    
    Args:
        principal (float): Initial loan amount
        annual_rate (float): Annual interest rate as a decimal
        payments (list): List of payment amounts
    """
    monthly_rate = annual_rate / 12
    current_balance = principal
    
    print(f"Loan Amount: ${principal:,.2f}")
    print(f"Annual Interest Rate: {annual_rate:.1%}")
    print(f"Monthly Interest Rate: {monthly_rate:.4%}")
    print("\n" + "="*70)
    print(f"{'Payment':<8} {'Amount':<10} {'Interest':<10} {'Principal':<10} {'Balance':<10}")
    print("="*70)
    
    for i, payment in enumerate(payments, 1):
        interest = current_balance * monthly_rate
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
    
    # Calculate balances
    balances = calculate_loan_balances(loan_amount, interest_rate, monthly_payments)
    
    print(f"\nBalances after each payment: {balances}")
    
    print("\nDetailed Payment Schedule:")
    print_payment_schedule(loan_amount, interest_rate, monthly_payments)
