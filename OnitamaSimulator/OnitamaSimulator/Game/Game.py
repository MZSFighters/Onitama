from Board import Board
from Player import Player
from Card import Card

class Game:

    """
    A class used to represent a single Onitama Game
    ...

    Attributes

    Player: player1, player2 
    Board: board 
    Card: neutralCard
    ----------
    Methods
    -------

    Game(): Initiates game by distributing two cards to each player (Player.Cards) and neutralCard, gives each player a colour,
            setups board, and enter while loop that lasts til someone wins the game

    """

    def __init__(self, gameState="N02000103044240414344NNNNN", gameStates=[], player1Name="Player1", player2Name= "Player2") -> None:
        '''
        Constructor for a game instance.
        ------------------------------
        Parameters
            gameState: String - specifies the desired state of the game we want to create. (See documentation for details)
            player1Name: String - specifies desired username of player1 while in game
            player2Name: String - specifies desired username of player2 while in game
        
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
        
        self.startGame(gameState[0]) #start the game

    #Methods

    def startGame(self, turn)->None:
        
        if (turn=='0'):
            self.turnCount=0 
        elif (turn =='1'):
            self.turnCount=1
        else: #select turn in normal way 

            if (self.player1.colour == self.neutralCard.colour):
                    self.turnCount=0
            else:
                self.turnCount=1

        self.gameStates.append(self.getGameState(self)) #Initial game state

        while (True): # while True game is running
            print(self.gameStates)

            # player can return to previous round

            if (input("would you like to reload to a previous round?")=="yes"):
                i = int(input("how many rounds back would you like to go?"))
                self.returnToPreviousGameState(i)

            while(True):

                if self.turnCount%2==0:
                    player, opp=self.player1, self.player2
                else:
                    player, opp=self.player2, self.player1

                print("The current board is") # Show the current board
                self.board.printBoard()

                
                print(" The neutral card is") # print neutral cards
                print(self.neutralCard)

                print("The opposition has the following cards") # print the opposition's cards
                print(opp.cards[0], opp.cards[1])

                print("Finally, your own cards are") # print the player's cards
                print(player.cards[0], player.cards[1])

                selectedCard = self.userSelectCard(player) #  let the user select a card 

                selectedPiece =self.userSelectPiece(self, player) # let user a chooses a piece
                
                possibleMoves = player.previewMoves(selectedCard,selectedPiece,self.board) # let user see all possible moves

                if (len(possibleMoves)==0): # there are no valid moves, player should reselect piece and card
                    print("No valid moves")


                if (input("Would you like to play one of these moves (yes or no)")=="yes"): # player can decide not to play a move

                    takePiece = player.MakeMove(possibleMoves,self.board, selectedPiece)
                    if (takePiece != None):
                        self.deletePiece(takePiece)
                        print("Took piece at tile : ", int(takePiece.row), " ", int(takePiece.col))

                    #reinit the board after the move
                    self.board = Board(self.player1, self.player2)
                    self.board.printBoard()

                    # swap neutral card with card played
                    self.neutralCard, player.cards[player.cards.index(selectedCard) ] = selectedCard, self.neutralCard

                    self.turnCount= self.turnCount+1
                    #update gamestate
                    self.gameStates.append(self.getGameState(self))
                    break

    # Methods 

    ## Methods for game initialization

    @staticmethod
    def handOutCards(self, cardString):
        '''
        A function which hands out player1's cards, player2's cards and the neutral card
        ------------------------------
        Parameters
            cardString: String - specifies desired cards for the game (documentation for more detail) 
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
    def userSelectCard(player):
        '''Function that allows the user to select a card from his hand'''
        while (True):
            val = input("Which card would you like to use (0 or 1) ?")
            if (val=='0' or val=='1'):
                return player.cards[int(val)]
            else:
                print("You selected an invalid option. Please try again")

    @staticmethod
    def userSelectPiece(self, player):
        '''Function that allows the user to select one of their pawns'''
        while True:

            self.board.printBoard()
            print("Your pieces are at the following positions")
            for piece in player.pieces:
                print(piece.row, piece.col)

            selectedPiece = input(" Which piece would you like to select?")

            row = int(selectedPiece[0])
            col =int(selectedPiece[2])

            for piece in player.pieces:
                if piece.row == row and piece.col ==col:
                    return piece
                
            print("Invalid coordinates given, please try again")

    def deletePiece(self, piece):
        '''
        removes piece from the game 
        ---------
        piece:Piece - piece to be removed from the game
        '''
        for player in [self.player1, self.player2]:
            for userPiece in player.pieces:
                if userPiece== piece:
                    player.pieces.remove(userPiece)
                    return

    def WinCon():
        pass
        # need to check if either Sensei is taken.
        

        # need to check if arch has been reached.

    @staticmethod
    def getGameState(self):
        '''
        returns the gameState string for the current game
        '''
        gameState =""
        #get the turn count
        gameState+=(str(self.turnCount%2))
        
        #next we get the coordiantes of the pieces of the players first coordinates of each player's pieces is the master
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
        Allows a user to return to a previous round in their current game
        -----
        Parameter
        i: int - how many rounds back 
        '''

        if i>= len(self.gameStates ) :
            print("Can not go back more turns than currently played!" )
            return 
        
        if len(self.gameStates)==1:
            print("This is far back as this game goes!")
            return 
        
        else:
            return Game(self.gameStates[len(self.gameStates)-i-1], self.gameStates[:len(self.gameStates)-i-1])


game = Game()


