from GameEngine.Card import Card
from GameEngine.Piece import Piece
from GameEngine.Board import Board
import copy

class Player:

    """
    A class used to represent a player.
    ...
    ----------
    Attributes

    Boolean Colour: Blue is True, red is False -> should be newly assigned each new game
    cards:  A list of two cards belonging to the player
    List(Piece) pieces: A list of all Pieces beloning to a player

    ----------
    Methods
    -------
    colour(): returns the colour of the player
    """

    def __init__(self, name="testName", colour= True):
        self.name = name
        self.colour = colour
        self.cards =[]
        self.pieces = []

    def givePieces(self, coordinates):
        '''
        Initializes the List of Pieces for a player where each piece is placed at a coordinate given by the string coordinates 
        ----------
        Parameters:
        coordinates: string - a 10 character string where each pair of characters represents the coordinates of some piece.
                              the master piece is always represented by coordinates[4], coordinates[5]

        '''
        pieces=[]

        for i in range(0, len(coordinates), 2):
            if coordinates[i]=='N': # this piece is no longer on the board
                continue
            else:
                if (i==0):
                    pieces.append(Piece(self.colour,True, int(coordinates[i]), int(coordinates[i+1])))
                else:
                    pieces.append(Piece( self.colour,False, int(coordinates[i]), int(coordinates[i+1]))) 

        self.pieces=pieces               

    def PrintPieces(self):
        for piece in self.pieces:
            print("player " , self.colour , "piece :" , piece.col,piece.row)

    #Utility Functions
    def getColour(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"
