def librarySystem():
    print("Welcome to the Library System!")
    print("Options: checkout, return, search, exit")
    
    while True:
        action = input("Enter an action (checkout, return, search, exit): ").strip().lower()
        item = input("Enter the item (e.g., book title or ID): ").strip()
        user_role = input("Enter your role (member, librarian): ").strip().lower()
        
        match action, item, user_role:
            case 'checkout', _, 'member' | 'librarian':
                print(f"'{item}' has been checked out.\n")
            
            case 'return', _, 'member' | 'librarian':
                print(f"'{item}' has been returned to the library.\n")
                
            case 'search', _, _:
                print(f"Searching for '{item}' in the catalog.\n")
                
            case 'exit', _, _:
                print("Exiting the library system.\n")
                break

            case _, _, _:
                print("Invalid command or insufficient permissions. Please try again.\n")

# Run the system
librarySystem()




def library_system():
    print("Welcome to the Library System!")
    print("Options: checkout, return, search, exit")
    
    while True:
        action = input("Enter an action (checkout, return, search, exit): ").strip().lower()
        item = input("Enter the item (e.g., book title or ID): ").strip()
        user_role = input("Enter your role (member, librarian): ").strip().lower()
        
        # Debug: Print the inputs to check them
        print(f"Debug - Action: {action}, Item: {item}, Role: {user_role}")
        
        # Check for each action and role combination
        if action == 'checkout' and (user_role == 'member' or user_role == 'librarian'):
            print(f"'{item}' has been checked out.\n")
        
        elif action == 'return' and (user_role == 'member' or user_role == 'librarian'):
            print(f"'{item}' has been returned to the library.\n")
        
        elif action == 'search':
            print(f"Searching for '{item}' in the catalog.\n")
        
        elif action == 'exit':
            print("Exiting the library system.\n")
            break  # Exits the loop and ends the program
        
        else:
            print("Invalid command or insufficient permissions. Please try again.\n")

# Run the system
library_system()




