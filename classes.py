

class Board:
    def __init__(self, arr):
        self.arr = arr
    
    def printBoard(self):
        for i in range(5):
            for j in range(5):
                print(str(arr[i][j].Value()),end=" ")
            print("")

class Player:
    def __init__(self, name, boolea, card1, card2):
        self.name = name
        self.colour = boolea
        self.card1 = card1
        self.card2 = card2
    
    def colour(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"
    




class Piece:
    def __init__(self, boo, player):
        self.boo = boo
        
    def isSensei(self):
        if(self.boo == True):
            return True
        else:
            return False



class Tile:
    def __init__(self, piece, coord_x, coord_y):
       self.piece = piece
       self.coord_x = coord_x
       self.coord_y = coord_y
       
    def isSenseiSeat(self):
        if(self.coord_x == 0 and self.coord_y == 2):
            return True
        elif(self.coord_x == 4 and self.coord_y == 2):
            return True
        else:
            return False
    
    def Value(self):
        if(self.piece == 0):
            return 0
        else:
            return 1
       
def initialise():
    array = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
    p = Piece(False, 1)
    p2 = Piece(True, 1)
    p3 = 0
    for i in range(5):
        for j in range(5):
            if(i ==0 or i==4):
                if(j == 2):
                    t = Tile(p2, i, j)
                else:
                    t = Tile(p, i, j)
                array[i][j] = t
            else:
                t = Tile(p3, i, j)
                array[i][j] = t
    return array
                
        
p = Piece(False, 1)
t = Tile(p, 4, 3)

boole = t.isSenseiSeat()
print(boole)
pie = t.piece.isSensei()
print(pie)
