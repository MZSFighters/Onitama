import Card
class Player:

    """
    A class used to represent a player.
    ...
    ----------
    Attributes

    Boolean Colour: Blue is True, red is False -> should be newly assigned each new game
    Two Cards (String): Two cards that belong to this player. 

    ----------
    Methods
    -------
    colour(): returns the colour of the player
    
    """
    
    def __init__(self, name, colour, card1, card2):
        self.name = name
        self.colour = colour
        self.card1 = card1
        self.card2 = card2
    
    def colour(self):
        if(self.colour == True):
            return "Red"
        else:
            return "Blue"
