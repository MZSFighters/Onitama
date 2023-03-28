def mainMenu():
    print("Welcome to Onitama!")
    print("1. Play")
    print("2. Load saved game")
    print("3. How to play")
    print("4. Add your custom cards here!!")
    print("5. High Score/Leaderboard")
    print("6. Settings")
    print("7. Exit")
    print("Enter your choice (1-7): ")

def playMenu():
    print("Select game mode:")
    print("1. Player vs AI")
    print("2. Player vs Player")
    print("3. Back to main menu")
    print("Enter your choice (1-3): ")

def howToPlayMenu():
    print("Instructions on how to play the Onitama Game Simulator:")
    print(" ")
    print("Onitama is a two-player abstract strategy game.")
    print("The goal is to capture your opponent's master pawn or move your own master pawn onto your opponent's starting space.")
    print("Players take turns moving one of their pawns according to the movement card they have.")
    print("There are five movement cards in play each game, two for each player and one neutral card.")
    print("Each movement card shows two possible moves for any pawn on the board.")
    print("A pawn may move any number of spaces in a straight line in any direction shown on the card, but cannot move through or onto any of their own pawns.")
    print("If a pawn lands on a space occupied by an opponent's pawn, that pawn is captured and removed from the board.")
    print("If a player cannot make a move on their turn, they lose the game.")
    print("Good luck!")
    print(" ")
    print("1. Back to main menu")
    print("Enter 1 to go back to main menu: ")

def settingsMenu():
    print("Game settings:")
    print("1. AI Difficulty")
    print("2. Sound")
    print("3. Credits")
    print("4. Help")
    print("5. Back to main menu")
    print("Enter your choice (1-5): ")

def AIDifficultyMenu():
    print("Choose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Back to settings menu")
    print("Enter your choice (1-4): ")

def soundMenu():
    print("Sound settings:")
    print("1. On")
    print("2. Off")
    print("3. Back to settings menu")
    print("Enter your choice (1-3): ")

def creditsMenu():
    print("Onitama")
    print("Developed by Mohammad Zaid Moonsamy, Ulrich Main, Muhammad Omar, Lefa Moraba, Tumi and Nkosana Kasi")
    print("Artwork by [Artist Name]")
    print("Music by [Musician Name]")
    print("Sound Effects by [Sound Designer Name]")
    print("Special Thanks to [Special Thanks List]")
    print("Thank you for playing Onitama!")
    print("1. Back to settings menu")
    print("Enter 1 to go back to settings): ")

def helpMenu():
    print("Help:")
    print("For more help please contact:")
    print("Mohammad Zaid Moonsamy at 2433079@students.wits.ac.za")
    print("UlrichMain at 1701173@students.wits.ac.za")
    print("Muhammad Omar at 1417565@students.wits.ac.za")
    print("Lefa Moraba at 2346902@students.wits.ac.za")
    print("Tumi at 2180153@students.wits.ac.za")
    print("1. Back to settings menu")
    print("Enter 1 to go back to settings): ")

def customCardMenu():
    print("1. Add a card")
    print("2. Edit a card")
    print("3. Delete a card")
    print("4. Back to main menu")
    print("Enter your choice (1-4): ")
