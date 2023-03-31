import Piece

class Tile:
    """
    A class used to represents a tile on the Onitama board
    ...

    ----------
    Attributes
    
    Piece piece: piece located on this tile
    Integer row, col

    ----------
    Methods
    -------
       
    isMasterSeat(): This method checks if the tile at the given (row,col) coordinate is a master seat/tile or not. It returns true if it is.
    
    Value(): This method checks if a piece exists on the (row,col) coordinate. If yes it returns 1 otherwise a 0. This helps to print the grid.
    """
    
    #Methods
    
    def __init__(self, piece, row, col):
       self.piece = piece
       self.row = row
       self.col = col
       
    def isMasterSeat(self):
        if(self.row == 0 and self.col == 2):
            return True
        elif(self.row == 4 and self.col == 2):
            return True
        else:
            return False
    
    def Value(self):
        if(self.piece == None):
            return 0
        else:
            if (self.piece.colour):
                return 1
            else:
                return 2
