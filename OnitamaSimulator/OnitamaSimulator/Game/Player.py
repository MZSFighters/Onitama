from Card import Card
from Piece import Piece
class Player:

    """
    A class used to represent a player.
    ...
    ----------
    Attributes

    Boolean Colour: Blue is True, red is False -> should be newly assigned each new game
    card1, card2: The two cards that belong to the player
    List(Pieces) pieces: A list of all Pieces beloning to a player

    ----------
    Methods
    -------
    colour(): returns the colour of the player
    givePieces(): creates all the pieces belonging to a player and stores them in self.pieces
    
    """

    def __init__(self, name="testName", colour= True):
        self.name = name
        self.colour = colour
        self.card1 = Card.selectCard()
        self.card2 = Card.selectCard()
        self.pieces = None


    def givePieces(self):
        '''Initializes the List of Pieces for a player'''
        if (self.colour==True):
            row=0
        else:
            row=4

        pieceList =[]
        for i in range(0,5):
            if (i==2): #master piece     
                pieceList.append(Piece(self.colour, True,row, i))
            else:    
                pieceList.append(Piece(self.colour, False,row, i))
        
        self.pieces=pieceList


    #Utility Functions
    def colour(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"

