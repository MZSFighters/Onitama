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

    def startGame(self):
        '''start the Game'''
        turnNumber=0 # Even turn number means its players1 turn, odd means player2 turn

        if self.player1.colour!= self.neutralCard.colour:
            turnNumber=1

        while (True):

            if (turnNumber%2==0):
                player = self.player1
            else:
                player = self.player2
                

            while(True):
                #  let the user select a card 
                selectedCard = self.userSelectCard(player)

                # Now a user chooses a piece
                selectedPiece =self.userSelectPawn(self, player)

                #Show available moves for that card and piece
                # showavailablemoves(selectedCard, selectedPiece)


                break



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
    def userSelectPawn(self, player):
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
                








                    

game = Game()
game.startGame()



