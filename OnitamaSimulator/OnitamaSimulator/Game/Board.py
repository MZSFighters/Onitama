import Tile
import Piece

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
    
    initialise(): we can call initialise method to give us the initial state of the board when the user starts the game.
    
    """

    #Attributes
    board=None;

    #Methods



class Board:
    def __init__(self, arr) -> None:
        self.arr = arr
    
    def printBoard(self):
        for i in range(5):
            for j in range(5):
                print(str(self.arr[i][j].Value()),end=" ")           # arr[i][j] is the tile and we are calling a function of tile called Value()
            print("")
            
            
    def initialise(self):
        array = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]   # dummy array
        p = Piece(False, 1)         #isNotMaster pawn piece prototype
        p2 = Piece(True, 1)         #isMaster pawn piece prototype
        for i in range(5):
            for j in range(5):
                if(i ==0 or i==4):
                    if(j == 2):
                        t = Tile(p2, i, j)
                    else:
                        t = Tile(p, i, j)
                    array[i][j] = t
                else:
                    t = Tile(None, i, j)
                    array[i][j] = t
        self.arr = array
        return array                #returns an array containing tiles

