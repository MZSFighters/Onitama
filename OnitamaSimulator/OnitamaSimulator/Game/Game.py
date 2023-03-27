from Board import Board
from Player import Player
from Card import Card
from Piece import Piece
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

    # Attributes
    player1 = None
    player2= None
    board=None
    neutralCard=None
    
    #Methods

    def __init__(self, Player1Name="Player1", Player2Name= "Player2") -> None:
        '''Constructor for a new game'''
        # Make The Deck
        Card.makeDeck()
        # Make the players
        self.player1 =Player(Player1Name, True )
        self.player2 =Player(Player1Name, False )
        #Give each player their set of pieces
        self.player1.givePieces()
        self.player2.givePieces()
        #Populate the  board with their pieces
        self.board = Board(self.player1, self.player2)
        #set neutral card
        self.neutralCard = Card.selectCard()

    def startGame(self):
        '''start the Game'''
        turnNumber=0 # Even turn number means its players1 turn, odd means player2 turn
        self.board.printBoard()
        if self.player1.colour!= self.neutralCard.colour:
            turnNumber=1

        while (True):

            if (turnNumber%2==0):
                player = self.player1
            else:
                player = self.player2
                

            # Now let the user select a card 
            selectedCard = self.userSelectCard(player)
            # Let the user select a piece
            selectedPiece = self.userSelectPiece(player)
            # Show Possible Moves to the player
            player.previewMoves(selectedCard,selectedPiece,self.board)


            break
        
    @staticmethod
    def userSelectCard(player):
            '''Function that allows the user to select a card from his hand'''
            #Print their cards
            player.printCards()
            while (True):
                val = int(input("Which card would you like to use (0 or 1) ?"))
                if (val==0 or val==1):
                    return player.cards[val]
                else:
                    print("You selected an invalid option. Please try again")

    @staticmethod                
    def userSelectPiece(player:Player):
        #Player uses xy co-ord to select piece
        while(True):
            valx = int(input("Enter piece x position"))
            valy = int(input("Enter piece y position"))
            #Need to see if selected piece exists
            for piece in player.pieces:
                print(piece.col)
                print(piece.row)

                if (piece.row == valy and piece.col == valx):
                    #return the appropriate piece
                    return piece
            print("Enter a valid piece co-ordinate")    
        


    



game = Game()
game.startGame()



