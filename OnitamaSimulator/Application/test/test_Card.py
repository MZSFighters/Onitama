import os, sys
import unittest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append( parentdir+ '\\GameEngine')
from GameEngine.Card import Card

class testCard(unittest.TestCase):

    def test_makeDeck(self): 
        Card.makeDeck()
        # Assert that deck is initialized correctly
        self.assertIsNotNone(Card.Deck)

    def test_selectCard(self):
        Card.makeDeck()
        card = Card.selectCard(0)
        # Test that selectCard returns a card object
        self.assertIsInstance(card, Card)
        # Check that card returned is the expected card for a specific call i.e. paramater a integer instead of 'N' 

        self.assertEqual(Card.selectCard(0).name, Card.Deck[0].name)
        self.assertEqual(Card.selectCard(4).name, Card.Deck[4].name)

        # Assert that a random call returns a card 
        self.assertIsInstance(Card.selectCard('N'), Card)
    
    def test_selectSpecifiedCard(self):
        Card.makeDeck()
        self.assertEqual(Card._selectSpecifiedCard(len(Card.Deck), 0).name, Card.Deck[0].name)
        self.assertEqual(Card._selectSpecifiedCard(len(Card.Deck), 4).name, Card.Deck[4].name)

    def test_selectRandomCard(self):
        Card.makeDeck()

        # test that the function only returns a card not already in the game
        cardsSeen=[]
        for i in range(0 , len(Card.Deck)):
            card = Card._selectRandomCard(len(Card.Deck))
            self.assertNotIn(card, cardsSeen)
            cardsSeen.append(card)


    def test_addCustomCard(self):
        card = Card("TheSittingSiiter", True, [])
        Card.makeDeck()
        Card.addCustomCard(card)

        self.assertIn(card, Card.Deck)



    def test_listAllCards(self):
        # Assert that the function returns all cards in the deck

        seenCards  = Card.listAllCards(True)
        self.assertEqual(len(seenCards), len(Card.Deck))

    def test_colourValue(self):
        # card stub
        card = Card("john", True, [[1,0]])

        self.assertEqual("Blue", card.colourValue())
        
        card = Card("john", False, [[1,0]])
        self.assertEqual("Red", card.colourValue())

    def test__printMoveSet(self):
        pass
  

if __name__ =='__main__':
      
      unittest.main()

