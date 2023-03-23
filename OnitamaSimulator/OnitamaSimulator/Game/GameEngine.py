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


game = Game()
game.board.printBoard()


