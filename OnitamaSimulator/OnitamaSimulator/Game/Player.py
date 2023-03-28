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
        for move in card.moveset:
            #Need to flip move based on player, From the moves it looks like we assume we are player 2
            if (self.colour == True):
                move[1] = -1*move[1]
                move[0] = -1*move[0]
            #Check if the move is within the bounds of the board
            #And check to see if the tile is a friendly piece
            calcMoveRow = piece.row-move[0]
            calcMoveCol  = piece.col - move[1]
     
            if (((calcMoveRow < 5) and (calcMoveRow >= 0)) and  (calcMoveCol < 5 and calcMoveCol >= 0)):
                if (board.returnTile(calcMoveRow,calcMoveRow).Value() != intColor):
                    debugBoard[piece.row-move[0]][piece.col-move[1]]=7
                    returnArray.append([piece.row-move[0], piece.col-move[1]])

        #Printing board with possible mpves
        for row in range(5):
            for col in range(5):
                print(debugBoard[row][col] , end = ' ')
            print()
        #Return array of possible moves
        return returnArray
    
    def MakeMove(self, possibleMoves:int, board:Board, pieceFrom:Piece):
        """
        Takes in the pawn and the desired location \n
        Need to check if there is another piece in the way
        """
        for move in possibleMoves:
            print(move[0]," ", move[1])

        selectedMove = input(" Which move would you like to select?")
        row = int(selectedMove[0])
        col =int(selectedMove[2])
        #Now I need to make a move 
        #"to" demarcates the tile we are moving to, "from" is the piece&tile we are moving
        pieceFrom.row = row
        pieceFrom.col = col

    def printCard(self):
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
        for move in card.moveset:
            #Need to flip move based on player, From the moves it looks like we assume we are player 2
            if (self.colour == True):
                move[1] = -1*move[1]
                move[0] = -1*move[0]
            #Check if the move is within the bounds of the board
            #And check to see if the tile is a friendly piece
            calcMoveRow = piece.row-move[0]
            calcMoveCol  = piece.col - move[1]
     
            if (((calcMoveRow < 5) and (calcMoveRow >= 0)) and  (calcMoveCol < 5 and calcMoveCol >= 0)):
                if (board.returnTile(calcMoveRow,calcMoveRow).Value() != intColor):
                    debugBoard[piece.row-move[0]][piece.col-move[1]]=7
                    returnArray.append([piece.row-move[0], piece.col-move[1]])

        #Printing board with possible mpves
        for row in range(5):
            for col in range(5):
                print(debugBoard[row][col] , end = ' ')
            print()
        #Return array of possible moves
        return returnArray
    
    def MakeMove(self, possibleMoves:int, board:Board, pieceFrom:Piece):
        """
        Takes in the pawn and the desired location \n
        Need to check if there is another piece in the way
        """
        for move in possibleMoves:
            print(move[0]," ", move[1])

        selectedMove = input(" Which move would you like to select?")
        row = int(selectedMove[0])
        col =int(selectedMove[2])
        #Now I need to make a move 
        #"to" demarcates the tile we are moving to, "from" is the piece&tile we are moving
        pieceFrom.row = row
        pieceFrom.col = col

