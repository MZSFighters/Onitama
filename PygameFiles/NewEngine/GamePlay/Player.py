from GamePlay.Card import Card
from GamePlay.Piece import Piece
from GamePlay.Board import Board
from GamePlay.Constants import *
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

    def previewMoves(self ,card:Card, piece:Piece, board:Board) -> int:
        """
        A preview of possible moves the player can make
        \n
        Debugs an array where the possible moves are represented by 7s
        \n
        Returns a list of possible moves as 2d co ords
        
        """
        returnArray = [] # the array that returns possible moves that is used by the move function
        debugBoard:int = [[0]*len(board.arr) for i in range(len(board.arr[0]))] # the board that debugs the possible moves
        debugBoard[piece.row][piece.col]=2 
        #converting the board into an array of ints, i think that this should be part of the board code but i dont want to tamper with too many classes at once
        for row in range(5):
            for col in range(5):
                debugBoard[row][col] = board.arr[row][col].Value()
        
        intColor = 2
        if (self.colour):
            intColor = 1
        
        moves = copy.copy(card.moveset)
        for move in moves:
            #Need to flip move based on player, From the moves it looks like we assume we are player 2
            if (self.colour == True):
                calcMoveRow = piece.row + move[0]
                calcMoveCol  = piece.col + move[1]

            elif (self.colour == False):
                calcMoveRow = piece.row - move[0]
                calcMoveCol  = piece.col - move[1]
     

            #Check if the move is within the bounds of the board
            #And check to see if the tile is a friendly piece

            if (((calcMoveRow < 5) and (calcMoveRow >= 0)) and  (calcMoveCol < 5 and calcMoveCol >= 0)):

                if (board.returnTile(calcMoveRow,calcMoveCol).piece==None):

                    
                    debugBoard[calcMoveRow][calcMoveCol]=7
                    returnArray.append([calcMoveRow, calcMoveCol])   
                                     
                elif board.returnTile(calcMoveRow,calcMoveCol).piece.colour != self.colour  :

                    debugBoard[calcMoveRow][calcMoveCol]=7
                    returnArray.append([calcMoveRow, calcMoveCol])

        
        return returnArray
    
    def MakeMove(self, board:Board, pieceFrom:Piece,move_row,move_col):
        """
        Takes in the pawn and the desired location \n
        Need to check if there is another piece in the way
        """
  
        row,col = move_row,move_col
        pieceFrom.row = row
        pieceFrom.col = col
        if (board.returnTile(row,col).piece!= None):
            return board.returnTile(row,col).piece
 

    def PrintPieces(self):
        for piece in self.pieces:
            print("player " , self.colour , "piece :" , piece.col,piece.row)

    #Utility Functions
    def colour(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"
