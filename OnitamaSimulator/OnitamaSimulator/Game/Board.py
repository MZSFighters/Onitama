from Tile  import Tile
from Piece import Piece
from Player import Player

class Board:

    """
    A class used to represents the Onitama Board
    ...
    
    ----------
    Attributes

    arr (Tile) - An array which contains tiles with values such as 0 for no piece on the tile and 1 for a piece present on the tile

    ----------
    Methods
    -------
    
    printBoard(): prints the current state of the board as a 5 by 5 grid/matrix whenever the method is called upon.
                  ** When you print the board (0,0) is the top left 
    
    initialise(): we can call initialise method to give us the initial state of the board when the user starts the game.
    
    """

    def __init__(self, player1, player2) -> None:
        array = [[0, 0, 0, 0, 0] ,[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]   # dummy array
        # Initiate Array to be 2d array of empty tiles

        for i in range(0, 5):
            for j in range(0,5):
                array[i][j] = Tile(None, i, j)

        for playerPiece in player1.pieces:
            array[playerPiece.row][playerPiece.col].piece = playerPiece

        for playerPiece in player2.pieces:
            array[playerPiece.row][playerPiece.col].piece = playerPiece

        self.arr = array


    def returnTile(self, i,j):
        '''Returns the tile at the position i,j on the board'''
        return(self.arr[i][j])

    def printBoard(self):
        for i in range(5):
            for j in range(5):
                print(str(self.arr[i][j].Value()),end=" ")           # arr[i][j] is the tile and we are calling a function of tile called Value()
            print("")
            

