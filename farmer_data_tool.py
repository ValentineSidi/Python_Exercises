# Agribusiness Farmer Data Capturing Tool

# Dictionary to store all farmers' details
farmers_database = {}

print("=== Agribusiness Farmer Data Capturing Tool ===\n")

# Main loop to keep program running
while True:
    print("\nMenu:")
    print("1. Add new farmer")
    print("2. View farmer details")
    print("3. View all farmers")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        # Add new farmer
        print("\n--- Add New Farmer ---")
        name = input("Enter farmer's name: ")
        age = input("Enter farmer's age: ")
        location = input("Enter farmer's location: ")
        crops = input("Enter crops they farm: ")
        land_size = input("Enter size of land (in acres): ")
        
        # Store farmer details in dictionary
        farmers_database[name] = {
            "age": age,
            "location": location,
            "crops": crops,
            "land_size": land_size
        }
        
        print(f"\nFarmer '{name}' has been added successfully!")
    
    elif choice == "2":
        # View specific farmer details
        print("\n--- View Farmer Details ---")
        name = input("Enter farmer's name: ")
        
        if name in farmers_database:
            print(f"\n--- Details for {name} ---")
            print(f"Age: {farmers_database[name]['age']}")
            print(f"Location: {farmers_database[name]['location']}")
            print(f"Crops: {farmers_database[name]['crops']}")
            print(f"Land Size: {farmers_database[name]['land_size']} acres")
        else:
            print(f"\nFarmer '{name}' not found in database!")
    
    elif choice == "3":
        # View all farmers
        print("\n--- All Farmers in Database ---")
        if farmers_database:
            for farmer_name in farmers_database:
                print(f"\nName: {farmer_name}")
                print(f"  Age: {farmers_database[farmer_name]['age']}")
                print(f"  Location: {farmers_database[farmer_name]['location']}")
                print(f"  Crops: {farmers_database[farmer_name]['crops']}")
                print(f"  Land Size: {farmers_database[farmer_name]['land_size']} acres")
        else:
            print("No farmers in database yet!")
    
    elif choice == "4":
        # Exit program
        print("\nThank you for using the Farmer Data Capturing Tool!")
        break
    
    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")
