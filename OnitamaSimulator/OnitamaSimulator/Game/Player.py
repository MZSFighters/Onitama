from Card import Card
from Piece import Piece
from Board import Board
from Tile import Tile
import math
class Player:

    """
    A class used to represent a player.
    ...
    ----------
    Attributes

    Boolean Colour: Blue is True, red is False -> should be newly assigned each new game
    card1, card2: The two cards that belong to the player
    List(Piece) pieces: A list of all Pieces beloning to a player

    ----------
    Methods
    -------
    colour(): returns the colour of the player
    givePieces(): creates all the pieces belonging to a player and stores them in self.pieces
    
    """

    def __init__(self, name="testName", colour= True):
        self.name = name
        self.colour = colour
        self.cards =[Card.selectCard(), Card.selectCard()]
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

    def printCards(self):
        '''Prints a list of the user's card  
          --------
          Desired changes
            should print cards side by side
            '''
        for card in self.cards:
            card.printCard()

    #Utility Functions
    def colour(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"
        
    def previewMoves(self ,card:Card, piece:Piece, board:Board) -> int:
        """
        A preview of possible moves the player can make
        \n
        Debugs an array where the possible moves are represented by 7s
        \n
        Returns a list of possible moves as 2d co ords
        
        """
        returnArray = []
        debugBoard:int = [[0]*len(board.arr) for i in range(len(board.arr[0]))]
        debugBoard[piece.row][piece.col]=2 
        #converting the board into an array of ints, i think that this should be part of the board code but i dont want to tamper with too many classes at once
        for row in range(5):
            for col in range(5):
                debugBoard[row][col] = board.arr[row][col].Value()
            
        for move in card.moveset:
            #Need to flip move based on player, From the moves it looks like we assume we are player 2
            if (self.colour == 1):
                move[1] = -1*move[1]
                move[0] = -1*move[0]
            #Check if the move is within the bounds of the board
            if (((piece.row-move[0] < 5) and (piece.row-move[0] >= 0)) and  (piece.col - move[1] < 5 and piece.col - move[1] >= 0)):
                debugBoard[piece.row-move[0]][piece.col-move[1]]=7
                returnArray.append([piece.row-move[0], piece.col-move[1]])

        #Printing board with possible mpves
        for row in range(5):
            for col in range(5):
                print(debugBoard[row][col] , end = ' ')
            print()
        #Return array of possible moves
        return returnArray
    
    def MakeMove(self, possibleMoves:int):
        """
        Takes in the pawn and the desired location \n
        Need to check if there is another piece in the way
        """
