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
    def _selectCard(n):
        """
        helper function for selectCard.   
        ---------
        Parameters
        Integer n: size of current deck
        """

        card = Card.Deck[random.randint(0,n-1)]
        if (card.alreadyInGame):

            return(Card._selectCard(n))
            
        else:
            card.alreadyInGame=True
            return card
     
    @staticmethod
    def selectCard():
        """
        Returns a random unselected card from the deck.    
        ---------
        Parameters
        ---------
        Raises
        --------
        """

        if (Card.Deck==None):
            raise TypeError("Deck has not been made yet. Call makeDeck() ")
        else:
            return(Card._selectCard(len(Card.Deck)))

    @staticmethod    
    def selectSpecificCard(name):
        '''
        Returns card whose name matches the name parameter
        -------------
        Parameters
        name: String - name of the card wanted
        '''
        for card in Card.Deck:
            if (card.name==name):
                return card
        
    
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






