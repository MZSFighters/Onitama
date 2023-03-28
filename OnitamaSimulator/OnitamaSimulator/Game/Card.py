import random # for card selector function

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
    def _selectSpecifiedCard(n, cardNum):
        card = Card.Deck[cardNum]
        card.alreadyInGame =True
        return card

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
    
    
    def _printMoveSet(self):
        '''Prints a a board of all possible moves for a given card (assuming the pawn is at position (2,2))'''

        array = [[0, 0, 0, 0, 0] ,[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
        array[2][2]=2 
        for move in self.moveset:
            array[2-move[0]][2-move[1]]=1
        for row in array:
            print(row)

    def printCard(self):
        '''Prints the card in the same way the cards are shown in the original game'''
        print(self.name)
        self._printMoveSet()






