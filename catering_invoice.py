# Catering Company Invoice Management System
import os
from datetime import datetime

def create_invoice():
    """
    Creates a new invoice for a customer
    """
    print("\n--- Create New Invoice ---")
    
    # Get invoice details
    invoice_number = input("Enter invoice number: ")
    customer_name = input("Enter customer name: ")
    invoice_date = input("Enter invoice date [YYYY-MM-DD]: ")
    
    # Use today's date if none provided
    if invoice_date.strip() == "":
        invoice_date = datetime.now().strftime("%Y-%m-%d")
        print(f"Using today's date: {invoice_date}")
    
    # Collect items and prices
    items = []
    total_amount = 0
    
    num_items = int(input("\nHow many items to add: "))
    
    print("\nEnter item details:")
    for i in range(num_items):
        print(f"\nItem {i+1}:")
        item_name = input("  Item name: ")
        item_price = float(input("  Price: "))
        items.append({"name": item_name, "price": item_price})
        total_amount += item_price
    
    # Create invoice content
    invoice_content = "=" * 50 + "\n"
    invoice_content += "         CATERING COMPANY INVOICE\n"
    invoice_content += "=" * 50 + "\n\n"
    invoice_content += f"Invoice Number: {invoice_number}\n"
    invoice_content += f"Invoice Date: {invoice_date}\n"
    invoice_content += f"Customer Name: {customer_name}\n"
    invoice_content += "\n" + "-" * 50 + "\n"
    invoice_content += "ITEMS ORDERED:\n"
    invoice_content += "-" * 50 + "\n"
    
    for item in items:
        invoice_content += f"{item['name']:<30} Kshs. {item['price']:>10,.2f}\n"
    
    invoice_content += "-" * 50 + "\n"
    invoice_content += f"{'TOTAL AMOUNT:':<30} Kshs. {total_amount:>10,.2f}\n"
    invoice_content += "=" * 50 + "\n"
    
    # Save invoice to file with customer name
    filename = f"{customer_name.replace(' ', '_')}_invoice.txt"
    with open(filename, "w") as file:
        file.write(invoice_content)
    
    print(f"\nInvoice created successfully and saved as '{filename}'!")
    print(invoice_content)

def view_invoice():
    """
    Views an existing invoice by customer name
    """
    print("\n--- View Invoice ---")
    customer_name = input("Enter customer name: ")
    filename = f"{customer_name.replace(' ', '_')}_invoice.txt"
    
    if not os.path.exists(filename):
        print(f"\nNo invoice found for customer '{customer_name}'!")
        return
    
    # Read and display invoice
    with open(filename, "r") as file:
        invoice_content = file.read()
        print("\n" + invoice_content)

def update_invoice():
    """
    Updates an existing invoice - allows selective field updates
    """
    print("\n--- Update Invoice ---")
    customer_name = input("Enter customer name: ")
    old_filename = f"{customer_name.replace(' ', '_')}_invoice.txt"
    
    if not os.path.exists(old_filename):
        print(f"\nNo invoice found for customer '{customer_name}'!")
        return
    
    # Read current invoice data
    with open(old_filename, "r") as file:
        lines = file.readlines()
    
    # Extract current invoice details from file
    current_invoice_number = ""
    current_date = ""
    current_customer = customer_name
    current_items = []
    
    for i, line in enumerate(lines):
        if "Invoice Number:" in line:
            current_invoice_number = line.split(": ")[1].strip()
        elif "Invoice Date:" in line:
            current_date = line.split(": ")[1].strip()
        elif "Customer Name:" in line:
            current_customer = line.split(": ")[1].strip()
        elif "Kshs." in line and "TOTAL AMOUNT:" not in line and i > 10:
            # Extract item details
            parts = line.rsplit("Kshs.", 1)
            if len(parts) == 2:
                item_name = parts[0].strip()
                item_price = float(parts[1].strip().replace(",", ""))
                current_items.append({"name": item_name, "price": item_price})
    
    # Display current invoice
    print("\nCurrent Invoice:")
    with open(old_filename, "r") as file:
        print(file.read())
    
    # Display current items with numbers
    print("\nCurrent Items List:")
    for idx, item in enumerate(current_items, 1):
        print(f"{idx}. {item['name']} - Kshs. {item['price']:,.2f}")
    
    print("\n--- What would you like to update? ---")
    print("1. Invoice Number")
    print("2. Invoice Date")
    print("3. Customer Name")
    print("4. Items")
    print("5. Update All")
    
    choice = input("\nEnter your choice (1-5): ")
    
    # Update based on choice
    new_invoice_number = current_invoice_number
    new_date = current_date
    new_customer = current_customer
    new_items = current_items.copy()
    
    if choice == "1" or choice == "5":
        new_invoice_number = input(f"Enter new invoice number (current: {current_invoice_number}): ")
    
    if choice == "2" or choice == "5":
        new_date = input(f"Enter new invoice date [YYYY-MM-DD] (current: {current_date}): ")
        if new_date.strip() == "":
            new_date = current_date
    
    if choice == "3" or choice == "5":
        new_customer = input(f"Enter new customer name (current: {current_customer}): ")
    
    if choice == "4" or choice == "5":
        print("\nUpdate Items:")
        print("a. Add new items (keep existing)")
        print("b. Replace all items")
        print("c. Remove specific items")
        
        item_choice = input("Enter your choice (a/b/c): ").lower()
        
        if item_choice == "a":
            # Add new items to existing
            num_new = int(input("\nHow many new items to add: "))
            print("\nEnter new item details:")
            for i in range(num_new):
                print(f"\nItem {i+1}:")
                item_name = input("  Item name: ")
                item_price = float(input("  Price: "))
                new_items.append({"name": item_name, "price": item_price})
        
        elif item_choice == "b":
            # Replace all items
            new_items = []
            num_items = int(input("\nHow many items to add: "))
            print("\nEnter item details:")
            for i in range(num_items):
                print(f"\nItem {i+1}:")
                item_name = input("  Item name: ")
                item_price = float(input("  Price: "))
                new_items.append({"name": item_name, "price": item_price})
        
        elif item_choice == "c":
            # Remove specific items
            print("\nCurrent items:")
            for idx, item in enumerate(current_items, 1):
                print(f"{idx}. {item['name']} - Kshs. {item['price']:,.2f}")
            
            remove_indices = input("\nEnter item NUMBERS to remove (e.g., 1,3 or just 2): ")
            try:
                indices_to_remove = [int(x.strip()) - 1 for x in remove_indices.split(",")]
                new_items = [item for idx, item in enumerate(current_items) if idx not in indices_to_remove]
                
                if len(new_items) == 0:
                    print("Cannot remove all items! At least one item must remain.")
                    new_items = current_items.copy()
            except ValueError:
                print("Invalid input! Please enter numbers only (e.g., 1,2,3)")
                new_items = current_items.copy()
    
    # Calculate new total
    total_amount = sum(item["price"] for item in new_items)
    
    # Create updated invoice content
    invoice_content = "=" * 50 + "\n"
    invoice_content += "         CATERING COMPANY INVOICE\n"
    invoice_content += "=" * 50 + "\n\n"
    invoice_content += f"Invoice Number: {new_invoice_number}\n"
    invoice_content += f"Invoice Date: {new_date}\n"
    invoice_content += f"Customer Name: {new_customer}\n"
    invoice_content += "\n" + "-" * 50 + "\n"
    invoice_content += "ITEMS ORDERED:\n"
    invoice_content += "-" * 50 + "\n"
    
    for item in new_items:
        invoice_content += f"{item['name']:<30} Kshs. {item['price']:>10,.2f}\n"
    
    invoice_content += "-" * 50 + "\n"
    invoice_content += f"{'TOTAL AMOUNT:':<30} Kshs. {total_amount:>10,.2f}\n"
    invoice_content += "=" * 50 + "\n"
    
    # If customer name changed, delete old file and create new one
    new_filename = f"{new_customer.replace(' ', '_')}_invoice.txt"
    if new_filename != old_filename:
        os.remove(old_filename)
    
    # Save updated invoice
    with open(new_filename, "w") as file:
        file.write(invoice_content)
    
    print(f"\nInvoice updated successfully!")
    print(invoice_content)

def main():
    """
    Main menu for the invoice management system
    """
    print("=== Catering Company Invoice Management System ===\n")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Create new invoice")
        print("2. View invoice")
        print("3. Update invoice")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            create_invoice()
        
        elif choice == "2":
            view_invoice()
        
        elif choice == "3":
            update_invoice()
        
        elif choice == "4":
            print("\nThank you for using the Invoice Management System!")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
