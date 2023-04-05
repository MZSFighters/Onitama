import random # for card selector function
import re

class Card:
    """Class which represents a Card within the game

     ----------
     Attributes

     (static) Deck (Array of Cards) - the set of all Cards in the base game
     name(String) - The name of the card
     moveset(2D integer array) - all possible moves a card allows. Each move is is 2-vector [down/up, left/right] down is negative, left is negative
     Colour (Boolean) - True is Blue, red is False

     Internal Attributes
     alreadyInGame (Boolean) - card has already been picked in current game

     ------
     Methods

     makeDeck(): Makes the deck of Cards - must be called whenever a game is made -> plan to add to database/lib
     selectCard() Selects a new card from the deck
     """

     #Attributes
    Deck= None

    def __init__(self, name: str, colour: bool, moveset ) -> None:
        
        self.name = name
        self.moveset = moveset
        self.colour = colour
        self.alreadyInGame= False

    def __str__(self):
        print(self.name)
        print(self.colourValue())
        self._printMoveSet()
        print("------------------")
        return ""

#methods

    @staticmethod
    def makeDeck():
        """
        Makes the deck of cards for the game

        Parameters
        ----------
        Raises
        ------
        """
        Deck=[]
        Deck.append(Card( 'Tiger', True, [[-1,0], [2, 0]])) 
        Deck.append(Card( 'Crab', True, [[1,0], [0, 2], [0, -2]])) 
        Deck.append(Card( 'Dragon', False, [[-1,-1], [-1, 1], [1, -2], [1, -2]] ))
        Deck.append(Card( 'Boar', False, [[0,-1], [0, 1], [1, 0] ])) 
        Deck.append(Card( 'Elephant', False, [[0,1], [0, -1], [1,-1], [1, 1] ]))

        Card.Deck =Deck

    @staticmethod
    def selectCard( cardNum):
        """
        Returns a specified or a random unselected card from the deck.    
        ---------
        Parameters
        cardNum: String of size 1 - returns the card at index cardNum form the deck
                 if cardNum== 'N' picks a random card
        ---------

        """
        if (Card.Deck== None):
            raise TypeError("Deck is type None, call makeDeck()")

        if (cardNum=='N'):
            return(Card._selectRandomCard(len(Card.Deck) ))
        else:
            return (Card._selectSpecifiedCard(len(Card.Deck), int(cardNum) ))
   
    @staticmethod
    def _selectSpecifiedCard(n, cardNum):
        card = Card.Deck[cardNum]
        card.alreadyInGame =True
        return card

    @staticmethod
    def _selectRandomCard(n):
        """
        helper function for selectCard.   
        ---------
        Parameters
        Integer n: size of current deck
        """

        card = Card.Deck[random.randint(0,n-1)]
        if (card.alreadyInGame):

            return(Card._selectRandomCard(n))
            
        else:
            card.alreadyInGame=True
            return card
     
    @staticmethod    
    def selectSpecifiedCard(name):
        '''
        Returns card whose name matches the name parameter
        -------------
        Parameters
        name: String - name of the card wanted
        '''
        for card in Card.Deck:
            if (card.name==name):
                return card
        
    @staticmethod
    def addCustomCard():
        '''
        Allows a user to add their own custom card to the deck of cards
        ------
        Errors
        Deck can not be null when this function is called
        '''

        card = Card("", True, [])
        inp= input("What should the name of the card be?")
        card.name= inp
        while (True):

            inp= input("What colour should the card be? (Red or Blue)")
            if (inp.lower()!="red" and inp.lower()!="blue"):
                print("Invalid options please try again")

            else:
                if (inp.lower()=="red"):
                    card.colour = False
                else:
                    card.colour= True
                break

        addingMoreMoves=True
        while (addingMoreMoves):    
            card._printMoveSet()
            inp= input("Which coordinates (starting from the position shown below) should your cards be able to reach? insert as coordinates row col")
            r = re.compile('[0-4]\s[0-4]')

            if (r.match(inp)): #if valid format add it to the cards moveset
                row = int(inp[0])-2
                col = int(inp[2])-2
                card.moveset.append([row, col])

                inp= input("add another move? (yes or no)")
                if (inp.lower()=="no"):
                    addingMoreMoves=False

            else:
                print("Invalid option please try again")

        card.printCard()
        Card.Deck.append(card) 
        print("Your card has been added to the deck!")

    def listAllCards():
        '''
        Prints a list of all cards in the deck - call deck first
        '''
        for i in range(0, len(Card.Deck)):
            print(Card.Deck[i])


#Utility Functions

    def colourValue(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"
    def _printMoveSet(self):
        '''Prints a a board of all possible moves for a given card (assuming the pawn is at position (2,2))'''

        array = [[0, 0, 0, 0, 0] ,[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        array[2][2]=2 
        for move in self.moveset:
            array[2-move[0]][2-move[1]]=1
        
        for row in array:
            print(row)
