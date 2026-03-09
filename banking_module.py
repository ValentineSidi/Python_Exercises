# Banking Services Module
# Dictionary to store all bank accounts
bank_accounts = {}

def create_account(account_number, account_holder, initial_balance=0):
    """
    Creates a new bank account
    Parameters:
        account_number: Unique identifier for the account
        account_holder: Name of the account holder
        initial_balance: Starting balance (default is 0)
    """
    if account_number in bank_accounts:
        print(f"Account {account_number} already exists!")
        return False
    
    bank_accounts[account_number] = {
        "account_holder": account_holder,
        "balance": initial_balance
    }
    print(f"Account created successfully for {account_holder}")
    print(f"Account Number: {account_number}")
    print(f"Initial Balance: Kshs. {initial_balance:,.2f}")
    return True

def handle_deposit(account_number, amount):
    """
    Handles deposit transactions
    Parameters:
        account_number: Account to deposit into
        amount: Amount to deposit
    """
    if account_number not in bank_accounts:
        print(f"Account {account_number} does not exist!")
        return False
    
    if amount <= 0:
        print("Deposit amount must be greater than zero!")
        return False
    
    bank_accounts[account_number]["balance"] += amount
    print(f"Deposit successful!")
    print(f"Amount Deposited: Kshs. {amount:,.2f}")
    print(f"New Balance: Kshs. {bank_accounts[account_number]['balance']:,.2f}")
    return True

def handle_withdrawal(account_number, amount):
    """
    Handles withdrawal transactions
    Parameters:
        account_number: Account to withdraw from
        amount: Amount to withdraw
    """
    if account_number not in bank_accounts:
        print(f"Account {account_number} does not exist!")
        return False
    
    if amount <= 0:
        print("Withdrawal amount must be greater than zero!")
        return False
    
    if bank_accounts[account_number]["balance"] < amount:
        print("Insufficient funds!")
        print(f"Available Balance: Kshs. {bank_accounts[account_number]['balance']:,.2f}")
        return False
    
    bank_accounts[account_number]["balance"] -= amount
    print(f"Withdrawal successful!")
    print(f"Amount Withdrawn: Kshs. {amount:,.2f}")
    print(f"New Balance: Kshs. {bank_accounts[account_number]['balance']:,.2f}")
    return True

def calculate_loan_interest(principal, rate, time_years):
    """
    Calculates simple interest on loans
    Parameters:
        principal: Loan amount
        rate: Annual interest rate (in percentage)
        time_years: Loan period in years
    Returns:
        Dictionary with interest and total amount
    """
    interest = (principal * rate * time_years) / 100
    total_amount = principal + interest
    
    print(f"\n--- Loan Interest Calculation ---")
    print(f"Principal Amount: Kshs. {principal:,.2f}")
    print(f"Interest Rate: {rate}% per annum")
    print(f"Loan Period: {time_years} years")
    print(f"Interest Amount: Kshs. {interest:,.2f}")
    print(f"Total Amount to Repay: Kshs. {total_amount:,.2f}")
    
    return {
        "principal": principal,
        "interest": interest,
        "total_amount": total_amount
    }

def view_account(account_number):
    """
    View account details
    Parameters:
        account_number: Account to view
    """
    if account_number not in bank_accounts:
        print(f"Account {account_number} does not exist!")
        return False
    
    print(f"\n--- Account Details ---")
    print(f"Account Number: {account_number}")
    print(f"Account Holder: {bank_accounts[account_number]['account_holder']}")
    print(f"Current Balance: Kshs. {bank_accounts[account_number]['balance']:,.2f}")
    return True

# Main program to demonstrate the functions
def main():
    print("=== Bank Management System ===\n")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Calculate Loan Interest")
        print("5. View Account")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            print("\n--- Create New Account ---")
            acc_num = input("Enter account number: ")
            holder = input("Enter account holder name: ")
            initial = float(input("Enter initial deposit amount: "))
            create_account(acc_num, holder, initial)
        
        elif choice == "2":
            print("\n--- Deposit ---")
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            handle_deposit(acc_num, amount)
        
        elif choice == "3":
            print("\n--- Withdrawal ---")
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            handle_withdrawal(acc_num, amount)
        
        elif choice == "4":
            print("\n--- Loan Interest Calculator ---")
            principal = float(input("Enter loan amount: "))
            rate = float(input("Enter interest rate (% per annum): "))
            years = float(input("Enter loan period (years): "))
            calculate_loan_interest(principal, rate, years)
        
        elif choice == "5":
            print("\n--- View Account ---")
            acc_num = input("Enter account number: ")
            view_account(acc_num)
        
        elif choice == "6":
            print("\nThank you for using the Bank Management System!")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()
