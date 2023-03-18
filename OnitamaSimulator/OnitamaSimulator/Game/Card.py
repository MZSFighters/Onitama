
from logging import raiseExceptions #for error raises
import random # for card selector function

class Card:

    """Class which represents a Card within the game

     ----------
     Attributes

     (static) Deck (Array of Cards) - the set of all Cards in the base game
     name(String) - The name of the card
     moveset(2D integer array) - all possible moves a card allows. Each move is is 2-vector [down/up, left/right] down is negative, left is negative
     Colour (Boolean) - True is Blue, red is False
     alreadyInGame (Boolean) - card has already been picked in current game

     ------
     Methods

     makeDeck(): Makes the deck of Cards - must be called whenever a game is made -> plan to add to database/lib
     selectCard() Selects a new card from the deck
     """

     #Attributes
    Deck= None

    name= None
    moveset= None
    colour = None
    alreadyInGame=False;


    def __init__(self, name: str, colour: bool, moveset ) -> None:

       
        self.name = name
        self.moveset = moveset
        self.colour = colour


    @classmethod
    def makeDeck(self):
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

        self.Deck = Deck

    @classmethod
    def _selectCard(self, n):
        """
        helper function for selectCard.   
        ---------
        Parameters
        Integer n: size of current deck
        """

        card = self.Deck[random.randint(0,4)]
        if (card.alreadyInGame):

            return(self._selectCard(n))
            
        else:
            card.alreadyInGame=True
            return card
     
    @classmethod
    def selectCard(self):
        """
        Returns card from deck.    
        ---------
        Parameters
        ---------
        Raises
        --------
        Issues
        may need a list of already picked cards depending on implementation
        """

        if (self.Deck==None):
            raise TypeError("Deck has not been made yet. Call _makeDeck() ")

        else:
            return(self._selectCard(len(self.Deck)))

