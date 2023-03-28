def mainMenu():
    print("Welcome to Onitama!")
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Options")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

while True:
    choice = mainMenu()
    if choice == '1':
        print("Starting new game...")
        # Call function to start a new game
    elif choice == '2':
        print("Loading saved game...")
        # Call function to load a saved game
    elif choice == '3':
        print("Opening options menu...")
        # Call function to display options menu
    elif choice == '4':
        print("Exiting Onitama. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
