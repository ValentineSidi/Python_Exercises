# OUK Student Details Management System
import os
def add_student():
    """
    Captures student details and stores them in a file
    """
    print("\n--- Add New Student ---")
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    course = input("Enter course: ")
    year_of_study = input("Enter year of study: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    
    # Open file in append mode to add new student
    with open("ouk_students.txt", "a") as file:
        file.write(f"Name: {student_name}\n")
        file.write(f"Student ID: {student_id}\n")
        file.write(f"Course: {course}\n")
        file.write(f"Year of Study: {year_of_study}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone: {phone}\n")
        file.write("-" * 50 + "\n")
    
    print(f"\nStudent '{student_name}' added successfully!")

def display_all_students():
    """
    Displays all student details from the file
    """
    print("\n--- All OUK Students ---")
    
    # Check if file exists
    if not os.path.exists("ouk_students.txt"):
        print("No student records found!")
        return
    
    # Read and display all student details
    with open("ouk_students.txt", "r") as file:
        content = file.read()
        
        if content.strip() == "":
            print("No student records found!")
        else:
            print(content)

def main():
    """
    Main menu for the student management system
    """
    print("=== OUK Student Management System ===\n")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add new student")
        print("2. Display all students")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            add_student()
        
        elif choice == "2":
            display_all_students()
        
        elif choice == "3":
            print("\nThank you for using OUK Student Management System!")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 3.")

# Run the program
if __name__ == "__main__":
    main()
