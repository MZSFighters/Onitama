"""A class for the pawn piece
     ----------
     Attributes
     
     isMaster (Boolean) - To keep track of the master pawn piece
     colour (Boolean)
     ----------
     Methods

     colour() return colour of the piece
"""

class Piece:
    def __init__(self, colour, isMaster, row=0, col =0):
        self.isMaster = isMaster
        self.colour = colour
        self.row =row 
        self.col =col

    def setTile(self, tiles):
        '''Place piece on a tile'''

    def colour(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"
        
