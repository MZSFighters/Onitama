from GameEngine.Board import Board
from GameEngine.Player import Player
from GameEngine.Card import Card
from configparser import ConfigParser

class Game:

    """
    A class used to represent a single Onitama Game
    ...

    Attributes

    Player: player1, player2 
    Board: board 
    Card: neutralCard
    gameStates: Str List - list of current and all previous game states
    turnCount: int - the current turn number for the game
    ----------
    Methods
    -------

    Game(self, gameState, gameStates, player1Name, ppayer2Name): Initiates game by distributing two cards to each player
            (Player.Cards) and neutralCard, gives each player a colour, setups board, and enter while loop that lasts
            until someone wins the game 

    startGame(self, turn): Initializes and begins the gameplay loop

    handOutCards(self, cardString): Distributes cards from deck to players.

    userSelectCard(player): returns the card selected by a player for a turn

    userSelectPiece(self, player): returns the piece selected by player during a turn

    deletePiece(self, piece): Removes the piece specified from the game

    getGameState(self): returns a str of the current game state 

    returnToPreviousGameState(self,i): function that returns the game instance to a previous GameState
    """

    def __init__(self, gameState="N02000103044240414344NNNNN", gameStates=[], player1Name="Player1", player2Name= "Player2") -> None:
        '''
        Constructor for a game instance. \n
        ------------------------------
        Parameters \n

        gameState: str - the gameState we want to create, default value is an initial game \n
        player1Name: str - name of player1 \n
        player2Name: str - name of player 2 \n
        ----------------------------

        '''
        
        Card.makeDeck() # Make The Deck
        self.turnCount=0 #turn count
        self.gameStates=gameStates
        
        # Make the players
        self.player1 =Player(player1Name, True )
        self.player2 =Player(player2Name, False )

        #Give each player their set of pieces
        self.player1.givePieces(gameState[1:11])
        self.player2.givePieces(gameState[11:21] )

        Game.handOutCards(self, gameState[21:]) # hand out their cards + neutral card handled as well

        self.board = Board(self.player1, self.player2) #Populate the  board with players' pieces
        self.gameStates.append(self.getGameState(self)) #Initial game state added to list of all game states


    def startGame(self, turn:str)->None:
        """
        Initiates game loop \n
        -------
        Parameters:
        string: turn: '0' if player 1 starts, '1' if player 2 starts 'N' if default starting order
        """
        
        if (turn=='0'):
            self.turnCount=0 
        elif (turn =='1'):
            self.turnCount=1
        else: #select turn in normal way 

            if (self.player1.colour == self.neutralCard.colour):
                    self.turnCount=0
            else:
                self.turnCount=1

        while (True): # while True game is running

            while(True):
                            
                if (input("would you like to reload to a previous round?")=="yes"):# option for player to return to previous rounds
                    i = int(input("how many rounds back would you like to go? -1 to restart" ))
                    self.returnToPreviousGameState(i)

                if self.turnCount%2==0:
                    player, opp = self.player1, self.player2
                else:
                    player, opp = self.player2, self.player1

                print("The current board is") # Show the current board
                self.board.printBoard()

                
                print(" The neutral card is") # print neutral cards
                print(self.neutralCard)

                print("The opposition has the following cards") # print the opposition's cards
                print(opp.cards[0], opp.cards[1])

                print("Finally, your own cards are") # print the player's cards
                print(player.cards[0], player.cards[1])

                 #  Ask user which card they want and fetch it
                selectedCardNum = self.getSelectedCardFromUser(player)
                selectedCard = self.fetchSelectedCard(player,selectedCardNum)

                selectedPieceCoords = self.getSelectedPieceFromUser(self, player) # let user a chooses a piece
                selectedPiece = self.fetchSelectedPiece( player, selectedPieceCoords)
                
                possibleMoves = player.previewMoves(selectedCard,selectedPiece,self.board) # let user see all possible moves

                if (len(possibleMoves)==0): # there are no valid moves, player should reselect piece and card
                    input("No valid moves, press Enter to confirm")


                elif (input("Would you like to play one of these moves (yes or no)")=="yes"): # player can decide not to play a move

                    takePiece = player.MakeMove(possibleMoves,self.board, selectedPiece)
                    if (takePiece != None):
                        self.deletePiece(takePiece)
                        print("Took piece at tile : ", int(takePiece.row), " ", int(takePiece.col))

                    #reinit the board after the move
                    #debugging 
                    self.board = Board(self.player1, self.player2)
                    self.board.printBoard()
                   
                    # swap neutral card with card played
                    self.neutralCard, player.cards[player.cards.index(selectedCard) ] = selectedCard, self.neutralCard

                    #did a player win?
                    win = self.WinCon()
                    if(win == 1):
                        print("Player 1 wins")
                    elif(win == 2):
                        print("Player 2 wins")
                    elif(win == 0):
                        pass
                    if(win != 0):
                        print("game over")
                        return
                    self.turnCount= self.turnCount+1
                    #update gamestate
                    self.gameStates.append(self.getGameState(self))

                    #Save Game
                    if (input("Would you like to save current game?(yes/no)") == "yes"):
                        gameName = input("Enter name to save game as: ")
                        self.SaveGame(self.getGameState(self), gameName)
                        choice=input("Game Saved!\nWould you like to continue playing?(yes/no): ")
                        if choice != "yes":
                            return

                    break
                else:
                    continue
                break
                
    # Methods 

    ## Methods for game initialization
    @staticmethod
    def handOutCards(self, cardString):
        '''
        A function which hands out player1's cards, player2's cards and the neutral card \n
        ------------------------------
        Parameters
            cardString: String - specifies desired cards for the game (look at documentation for more detail) \n
        '''

        cards=[Card]*5
        #hand out specified cards first
        for i in range(0 , 5):
            if cardString[i]!= "N":
                cards[i]= Card.selectCard(cardString[i])


        # Now hand out random cards
        for i in range(0 , 5):
            if cardString[i]== "N":
                cards[i]= Card.selectCard(cardString[i])

        self.player1.cards = cards[0:2]
        self.player2.cards = cards[2:4]
        self.neutralCard =cards[-1]

    ## Methods used while in a turn (try to maintain order used)

    @staticmethod
    def getSelectedCardFromUser(player):
        '''
        Function that returns user input for which card they want to use as an integer
        '''

        while True:
            val = input("Which card would you like to use (0 or 1) ?")
            if (val=='0' or val=='1'):
                return int(val)
            else:
                print("You selected an invalid option. Please try again")
    @staticmethod
    def fetchSelectedCard(player, val):
        '''
        Function that returns a user's selected card \n
        '''
        return player.cards[val]


    @staticmethod
    def getSelectedPieceFromUser(self, player):
        '''
        Function that allows a user to select a piece they want to play
        '''

        while True:
            self.board.printBoard()
            print("Your pieces are at the following positions")
            for piece in player.pieces:
                print(piece.row, piece.col)

            selectedPiece = input(" Which piece would you like to select?")
            row = int(selectedPiece[0])
            col = int(selectedPiece[2])

            for piece in player.pieces:
                if piece.row == row and piece.col ==col:
                    return [row,col]
            
            print("Invalid coordinates given, please try again")

    @staticmethod
    def fetchSelectedPiece( player, coords):
        '''
        Function that allows the user to select one of their pawns \n
        -----------
        Parameters \n
        player: Player - the player instance currently selecting a Piece
        '''
        
        for piece in player.pieces:
            if piece.row == coords[0] and piece.col ==coords[1]:
                return piece
                            

    def deletePiece(self, piece):
        '''
        removes piece from the game \n
        ---------
        piece:Piece - piece to be removed from the game \n
        '''
        for player in [self.player1, self.player2]:
            for userPiece in player.pieces:
                if userPiece== piece:
                    player.pieces.remove(userPiece)
                    return

    def WinCon(self):
        # need to check if either Sensei is taken, or in arch
        dedSensei = True
        # Player 1 checks
        for player1 in self.player1.pieces:
            if (player1.col == 2 and player1.row == 4):
                print("p1 arch")
                return 1
            if(player1.isMaster == True):
               
                dedSensei = False
                break
        if(dedSensei == True):
            print("p2 take")
            return 2 # player 2 wins
        dedSensei = True
        #player 2
        for player2 in self.player2.pieces:
            if (player2.col == 2 and player2.row == 0):
                print("p2 arch")
                return 2
            if(player2.isMaster == True):
                
                dedSensei = False
                break
        if(dedSensei == True):
            print("p1 take")
            return 1 # player 1 wins
        return 0 

    @staticmethod
    def getGameState(self)-> str:
        '''
        returns the gameState for game as a string \n
        '''
        gameState =""
        #get the turn count
        gameState+=(str(self.turnCount%2))
        
        #next we get the coordinates of the pieces of the players first coordinates of each player's pieces is the master
        players =[self.player1, self.player2]
        for player in players:
            pieceString =["N"]*10
            i=2
            for piece in player.pieces:
                if (piece.isMaster ):
                    pieceString[0] = str(piece.row)
                    pieceString[1]= str(piece.col)
                else:
                    pieceString[i]= str(piece.row)
                    pieceString[i+1] = str(piece.col)
                    i=i+2

            gameState+= ''.join(pieceString)

        # Now we add the card numbers

        for player in players:
            for card in player.cards:
                gameState+= str(Card.Deck.index(card))

        # finally the neutral card
        gameState+= str(Card.Deck.index(self.neutralCard))

        return gameState

    ## Utility Functions
    def returnToPreviousGameState(self, i):
        '''
        Allows a user to return to a previous round in their current game \n
        -----
        Parameter
        i: int - how many turns back to go, -1 to restart game \n
        '''

        if (i==-1):
            return Game(self.gameStates[0], [])

        if i>= len(self.gameStates ) :
            print("Can not go back more turns than currently played!" )
            return 
        
        if len(self.gameStates)==1:
            print("This is far back as this game goes!")
            return 
        
        else:
            return Game(self.gameStates[len(self.gameStates)-i-1], self.gameStates[:len(self.gameStates)-i-1])

    def SaveGame(self, GameState,GameName):
        """
        Allows a user to save game state to config file \n
        -----
        Parameter
        GameState: string - GameString with state to be saved \n
        GameName: string - Name of the game to be saved,used to create new section in config file \n
        """
        #create ConfigParser object and read the config file
        config = ConfigParser()
        config.read("save_game_config.ini")

        #add info to be saved to config file
        config.add_section(GameName)
        config.set(GameName,"GameString",GameState)

        with open("save_game_config.ini", "w") as configfile:
            config.write(configfile)

