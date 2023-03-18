import random

# (x, y) Pair class for coordinates
class pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# The Board method gives us the initial board grid
def Board():
    Matrix= [[1 ,1,3,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,3,1,1]]
    return Matrix

# The Card method returns an array with 5 cards. 2->P1, 2->P2 and 1 for neutral card
def Card():
    d = {1:'GIRRAFE', 2:'DRAGON', 3:'RABBIT', 4:'TIGER', 5:'FROG', 6:'CRAB', 7:'ELEPHANT', 8:'GOOSE', 9:'ROOSTER', 10:'MONKEY', 13:'MANTIS', 12:'HORSE', 13:'OX', 14:'COBRA', 15:'EEL', 16:'BOAR'}
    
    arr = ["", "", "", "", ""]
    i= 0
    while(i < 5):
        arr[i] = random.choice(list(d.values()))
        for j in range(i):
            if arr[j] == arr[i]:
                i = i - 1
        i += 1
    return arr
    
# The coordinates returned if card was TIGER.
def coordinates(playcard, p1):
    x1 = p1.x
    y1 = p1.y
    if playcard == "TIGER":
        pair_1 = pair(x1 +1, y1)
        pair_2 = pair(x1 -2, y1)
        arr = [pair_1, pair_2]
        return arr

# Main method


#Initialisation
Matrix = []
Matrix = Board()
x = Card()

#Printing initial board + cards and asking for user input
for i in range(5):
    print(Matrix[i])
print("Player 1 Cards: " + x[0] + " and " + x[1])
print("Player 2 Cards: " + x[2] + " and " + x[3])
print("Neutral Card: " + x[4])
print("Player 1 goes first")
playcard = input("Which card do you want to play:")
playpawn = input("Which pawn do you want to play:")

# making (x,y) pairs with given input
split = playpawn.split(",")
p1 = pair(int(split[0]), int(split[1]))
vec = coordinates(playcard, p1)

# presenting the options to the user and asking user for which option to play
for i in range(len(vec)):
    print(str(i) + ". " + str(vec[i].x) + "," + str(vec[i].y))
num = int(input("please type the respective number:"))


if num == 0:
    Matrix[int(vec[0].x)][int(vec[0].y)] = 1
    Matrix[int(split[0])][int(split[1])] = 0
else:
    Matrix[vec[1].x][vec[1].y] = 1
    Matrix[int(split[0])][int(split[1])] = 0

# printing the matrix after the move
for i in range(5):
    print(Matrix[i])
