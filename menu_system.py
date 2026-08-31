def build_menu():
    """
    Prints the system menu options.
    No parameters, no return value.
    """
    print("1. Check Voltage")
    print("2. Check Resistance")
    print("3. Run Calibrator")
    print("4. Exit System")

def display_menu():
    """
    Handles the interaction loop:
    1. Calls build_menu() to show options.
    2. Reads user input.
    3. Processes choices 1-3 or exits on 4.
    """
    while True:
        # Display the menu options
        build_menu()
        
        # Get user choice
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # Process the choice
        if choice == 1:
            print("Action: Checking voltage...")
        elif choice == 2:
            print("Action: Checking resistance...")
        elif choice == 3:
            print("Action: Running calibrator...")
        elif choice == 4:
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    display_menu()