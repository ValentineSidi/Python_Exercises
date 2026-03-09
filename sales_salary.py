# Sales Company Employee Salary Calculator
# Retainer: Kshs. 25,000
# Commission based on sales amount

# Get employee information
employee_name = input("Enter employee name: ")
employee_number = input("Enter employee number: ")
sales = float(input("Enter total sales amount (Kshs): "))

# Base retainer amount
retainer = 25000

# Calculate commission based on sales
if sales <= 10000:
    commission = sales * 0.02  # 2% commission
elif sales > 10000 and sales <= 50000:
    commission = sales * 0.05  # 5% commission
elif sales > 50000 and sales <= 100000:
    commission = sales * 0.10  # 10% commission
else:  # sales > 100000
    commission = sales * 0.15  # 15% commission

# Calculate total salary
salary = retainer + commission

# Display employee salary information
print("\n--- Employee Salary Details ---")
print(f"Employee Name: {employee_name}")
print(f"Payroll Number: {employee_number}")
print(f"Total Salary for the Month: Kshs. {salary:,.2f}")
