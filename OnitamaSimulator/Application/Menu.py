from GameEngine import *
import UseEnv
import configparser
def mainMenu():
    print("Welcome to Onitama!")
    print("1. Play")
    print("2. Load saved game")
    print("3. How to play")
    print("4. Add your custom cards here!!")
    print("5. High Score/Leaderboard")
    print("6. Settings")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    list = ['1', '2', '3', '4', '5', '6', '7']

    if choice == '1':
        # Call a function which prints the play menu
        playMenu()

    elif choice == '2':
        # Call a function which loads saved games
        savedGamesMenu()

    elif choice == "3":
        # Call a function which prints instructions on how to play the game
        howToPlayMenu()

    elif choice == "4":
        # Call a function which prints card menu
        customCardMenu()

    elif choice == "5":
        # Call a function which prints the game's leaderboard
        leaderBoardMenu()

    elif choice == "6":
        # Call a function which prints the settings menu
        settingsMenu()

    elif choice == "7":
        # Call a function which ends the program
        exit()

    # If the user enters a invalid choice
    elif choice is not list:
        print("Invalid choice, please enter a valid choice")
        mainMenu()


def playMenu():
    print("Select game mode:")
    print("1. Player vs AI")
    print("2. Player vs Player")
    print("3. Back to main menu")
    print("4. AI vs AI ")
    choice = input("Enter your choice (1-3): ")

    list = ['1', '2', '3']

    if choice == '1':
        # Calls a fuction for the player vs ai  menu
        game = Game.Game()
        game.startGame(game.gameStates[0][0], "easy") #start the game

    elif choice == '2':
        print("Starting game...")
        # Call a function which starts the game
        game = Game.Game()
        game.startGame(game.gameStates[0][0], "Player2") #start the game

    elif choice == '3':
        # Call a function which takes you back to the main menu
        mainMenu()
    elif choice == '4':
        doEnv()

    # If the user enters a invalid choice
    elif choice is not list:
        print("Invalid choice, please enter a valid choice")
        playMenu()

def doEnv():
    envClass = UseEnv.UseEnv()
    envClass.DoTheEnv()


def playerVsAIMenu():
    print("Sorry this feature is not supported yet. We apologise for the inconvenience")
    choice = input("Enter 1 to go back to play menu: ")

    list = ['1']

    if choice == '1':
        playMenu()

    # If the user enters a invalid choice
    elif choice is not list:
        playerVsAIMenu()


def savedGamesMenu():

    print("Load Game Menu:")
    print("1. Load Game State")
    print("2. Delete Game State")
    print("3. Back To Main Menu")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':

        gameString = LoadGame()

        if gameString == "":
            savedGamesMenu()

        else:
            # start game at selected state
            game = Game.Game(gameString)

            # return to menu when loaded game is exited
            mainMenu()

    elif choice == '2':
        deleteMenu()
        savedGamesMenu()

    elif choice == '3':
        mainMenu()

    else:
        print("Invalid choice, please enter a valid choice")
        savedGamesMenu()


def howToPlayMenu():
    print("Instructions on how to play the Onitama Game Simulator:")
    print(" ")
    print("Onitama is a two-player abstract strategy game.")
    print("The goal is to capture your opponent's master pawn or move your own master pawn onto your opponent's starting space.")
    print("Players take turns moving one of their pawns according to the movement card they have.")
    print("There are five movement cards in play each game, two for each player and one neutral card.")
    print("Each movement card shows possible moves for any pawn on the board.")
    print("A pawn may move any number of spaces in any direction shown on the card,")
    print("given that making that move lands you outside the board or on top ofyour own pawn.")
    print("If a pawn lands on a space occupied by an opponent's pawn, that pawn is captured and removed from the board.")
    print("If a player cannot make a move on their turn, they lose the game.")
    print("Good luck!")
    print(" ")
    choice = input("Enter 1 to go back to main menu: ")

    list = ['1']

    # Call a function that will take you back to the main menu
    if choice == '1':
        mainMenu()

    # If the user enters a invalid choice
    elif choice is not list:
        print("Invalid choice, please enter a valid choice")
        howToPlayMenu()


def leaderBoardMenu():
    print("High Score/Leaderboard: ")
    print(" ")
    choice = input("Enter 1 to go back to main menu: ")

    list = ['1']

    if choice == '1':
        mainMenu()

    # If the user enters a invalid choice
    elif choice is not list:
        print("Invalid choice, please enter a valid choice")
        leaderBoardMenu()


def settingsMenu():
    print("Game settings:")
    print("1. AI Difficulty")
    print("2. Sound")
    print("3. Credits")
    print("4. Help")
    print("5. Back to main menu")
    choice = input("Enter your choice (1-5): ")

    list = ['1', '2', '3', '4', '5']

    if choice == '1':
        # Call a function which prints the ai difficulty menu
        AIDifficultyMenu()

    elif choice == '2':
        # Call a function which prints the sound menu
        soundMenu()

    elif choice == "3":
        # Call a function which prints credits for the game
        creditsMenu()

    elif choice == "4":
        # Call a function which prints the help menu
        helpMenu()

    elif choice == "5":
        # Call a function which will take you back to the main menu
        mainMenu()

    # If the user enters a invalid choice
    elif choice is not list:
        print("Invalid choice, please enter a valid choice")
        settingsMenu()


def AIDifficultyMenu():

    config = configparser.ConfigParser()
    config.read("main_menu_terminal.ini")

    config_data = config["DEFAULT"]

    myDict = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}

    print('\n'"Current Difficulty : " + config_data["AIDifficulty"])
    print("Choose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Back to settings menu")
    choice = input("Enter your choice (1-4): ")

    if choice == '1' or choice == '2' or choice == '3':
        update = str(myDict[choice])
        config.set("DEFAULT", 'AIDifficulty', update)
        with open("main_menu_terminal.ini", 'w') as f:
            config.write(f)
        AIDifficultyMenu()

    elif choice == '4':
        settingsMenu()
    else:
        print("Invalid choice. Please enter a valid choice")
        AIDifficultyMenu()

    # list = ['1', '2', '3', '4']

    # if choice == '1':
    #     # Set the AI difficulty level to easy
    #     print("The AI difficulty level is set to Easy")
    #     AIDifficultyMenu()

    # elif choice == '2':
    #     # Set the AI difficulty level to medium
    #     print("The AI difficulty level is set to Medium")
    #     AIDifficultyMenu()

    # elif choice == '3':
    #     # Set the AI difficulty level to hard
    #     print("The AI difficulty level is set to Hard")
    #     AIDifficultyMenu()

    # elif choice == '4':
    #     # Calls a function to take you back to the settings menu
    #     settingsMenu()

    # # If the user enters a invalid choice
    # elif choice is not list:
    #     print("Invalid choice, please enter a valid choice")
    #     AIDifficultyMenu()


def soundMenu():

    config = configparser.ConfigParser()
    config.read("main_menu_terminal.ini")

    config_data = config["DEFAULT"]

    print('\n'"Sound is currently : " + config_data["Sound"])
    print("Sound settings:")
    print("1. On")
    print("2. Off")
    print("3. Back to settings menu")
    choice = input("Enter your choice (1-3): ")

    myDict = {'1': 'On', '2': 'Off'}

    if choice == '1' or choice == '2':
        update = str(myDict[choice])
        config.set("DEFAULT", "Sound", update)
        with open("main_menu_terminal.ini", 'w') as f:
            config.write(f)
        soundMenu()
    elif choice == '3':
        # Calls a function to take you back to the settings menu
        settingsMenu()
    else:
        print("Invalid choice, please enter a valid choice")
        soundMenu()

    # list = ['1', '2', '3']

    # if choice == '1':
    #     # Turns on the sound
    #     print("Sound is turned on")
    #     soundMenu()

    # elif choice == '2':
    #     # Turns off the sound
    #     print("Sound is turned off")
    #     soundMenu()

    # elif choice == '3':

    #     # Calls a function to take you back to the settings menu
    #     settingsMenu()

    # # If the user enters a invalid choice
    # elif choice is not list:
    #     print("Invalid choice, please enter a valid choice")
    #     soundMenu()


def creditsMenu():
    print("Onitama")
    print(" ")
    print("Developed by Mohammad Zaid Moonsamy, Ulrich Main, Muhammad Omar, Lefa Moraba, Tumi and Nkosana Kasi")
    print("Artwork by Muhammad Omar and Ulrich Main")
    print("Music by Mohammad Zaid Moonsamy and Tumi")
    print("Sound Effects by Lefa Moraba")
    print("Special Thanks to Tamlin Love and Branden Ingram")
    print("Thank you for playing Onitama!")
    print(" ")
    choice = input("Enter 1 to go back to settings : ")

    list = ['1']

    if choice == '1':
        # Calls a function to take you back to the settings menu
        settingsMenu()

    # If the user enters a invalid choice
    elif choice is not list:
        print("Invalid choice, please enter a valid choice")
        creditsMenu()


def helpMenu():
    print("Help:")
    print(" ")
    print("For more help please contact:")
    print("Mohammad Zaid Moonsamy at 2433079@students.wits.ac.za")
    print("UlrichMain at 1701173@students.wits.ac.za")
    print("Muhammad Omar at 1417565@students.wits.ac.za")
    print("Lefa Moraba at 2346902@students.wits.ac.za")
    print("Tumi at 2180153@students.wits.ac.za")
    print(" ")
    choice = input("Enter 1 to go back to settings): ")

    list = ['1']

    if choice == '1':
        # Calls a function to take you back to the settings menu
        settingsMenu()

    # If the user enters a invalid choice
    elif choice is not list:
        print("Invalid choice, please enter a valid choice")
        helpMenu()


def customCardMenu():
    print("1. Add a card")
    print("2. Edit a card")
    print("3. Delete a card")
    print("4. See all cards currently in the game")
    print("5. Back to main menu")
    choice = input("Enter your choice (1-4): ")

    list = ['1', '2', '3', '4', '5']

    if choice == '1':
        # Call a function to add a card
        print("Adding a new card")
        Card.Card.addCustomCard()

    elif choice == '2':
        # Call a function to edit existing card
        print("Edit a existing card")

    elif choice == '3':
        # Call a function to delete a card
        print("Delete a existing card")

    elif choice == '4':
        # Call a function to take you back to the main menu
        Card.Card.makeDeck()
        Card.Card.listAllCards()

    elif choice =='5':
        mainMenu()

    # If the user enters a invalid choice
    elif choice is not list:
        print("Invalid choice, please enter a valid choice")
        customCardMenu()


def LoadGame() -> str:
    """
    Displays Saved Games and allows user to select one

    returns the gameState for game as a string \n
    """

    config = config.ConfigParser()
    config.read("save_game_config.ini")

    print("Available Games: ")
    for section in config.sections():
        print(section)

    if (len(config.sections()) == 0):
        print("No saved Games!")
        return ""

    gamename = input("Write the name of the game you wish to load(Enter 0 To Go Back): ")

    if gamename == '0':
        return ""

    try:
        gameData = config[gamename]
    except:
        print("Game not found!Please enter a name from the list.(Case Sensitive!)")
        LoadGame()
    gamestring = gameData['GameString']
    return gamestring


def deleteMenu():
    """
    Displays Saved Games and allows user to select one to delete(remove from config file)

    """

    config = config.ConfigParser()
    config.read("save_game_config.ini")

    print("Available Games: ")
    for section in config.sections():
        print(section)

    if (len(config.sections()) == 0):
        print("No saved Games!")
        return

    gamename = input("Write the name of the game you wish to delete(Enter 0 To Go Back): ")

    if gamename == '0':
        return

    try:  # check if given name is a valid config file section
        gameData = config[gamename]
    except:
        print("Game not found!Please enter a name from the list.(case sensitive)")
        deleteMenu()

    # remove game
    config.remove_section(gamename)

    # update config file
    with open("save_game_config.ini", "w") as configfile:
        config.write(configfile)

    print("Game Removed!")


mainMenu()
