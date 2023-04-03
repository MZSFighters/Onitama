"""A class for the pawn piece
     ----------
     Attributes
     
     isMaster (Boolean) - To keep track of the master pawn piece
     colour (Boolean)
     row = row of board piece currently occupies
     col = col of board piece currently occupies
     ----------
     Methods

     colour(): Boolean - returns colour of the piece
     setTile(tile): void - places the piece on the specified tile
"""

class Piece:
    def __init__(self, colour, isMaster, row=0, col =0):
        self.isMaster = isMaster
        self.colour = colour
        self.row =row 
        self.col =col

    def setTile(self, tile):
        '''Place piece on a tile'''

    def colour(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"
        
