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

    def __init__(self, gameState="N02000103044240414344NNNNN", player1Name="Player1", player2Name= "Player2") -> None:
        
        '''
        Constructor for a game instance.
        ------------------------------
        Parameters
            gameState: String - specifies the desired state of the game we want to create. (See documentation for details)
            player1Name: String - specifies desired username of player1 while in game
            player2Name: String - specifies desired username of player2 while in game
        
        '''
        self.gameState = gameState #Initial game state
        Card.makeDeck() # Make The Deck
        self.turnCount=0 #turn count

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

        while (True):

            if (turn=='0'):
                self.turnCount=0 
            elif (turn =='1'):
                self.turnCount=1
            else: #select turn in normal way 

                if (self.player1.colour == self.neutralCard.colour):
                    self.turnCount=0
                else:
                    self.turnCount=1
                
            while(True):

                if self.turnCount%2==0:
                    player=self.player1
                else:
                    player=self.player2

                # should show all cards currently in game so opposition, neutral and their cards

                print(" The current neutral card is")
                self.neutralCard.printCard()

                #  let the user select a card 
                selectedCard = self.userSelectCard(player)

                # Now a user chooses a piece
                selectedPiece =self.userSelectPiece(self, player)
                possibleMoves = player.previewMoves(selectedCard,selectedPiece,self.board)

                #Show available moves for that card and piece
                # showavailablemoves(selectedCard, selectedPiece)
                player.MakeMove(possibleMoves,self.board, selectedPiece)

                #reinit the board after the move
                self.board = Board(self.player1, self.player2)
                self.board.printBoard()

                # swap neutral card with card played
                self.neutralCard, player.cards[player.cards.index(selectedCard) ] = selectedCard, self.neutralCard

                self.turnCount+=1
                #update gamestate
                self.gameState = self.getGameState(self)
                
            break
        
    @staticmethod
    def userSelectCard(player):
        '''Function that allows the user to select a card from his hand'''
        #Print their cards
        player.printCard()
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




game = Game()