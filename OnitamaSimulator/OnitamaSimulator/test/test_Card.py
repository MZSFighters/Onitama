import os, sys
import unittest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import GameEngine.Card as Card

class testCard(unittest.TestCase):

    def test_makeDeck(self):
        pass

    def test_selectCard(self):
        pass

    def test_selectSpecifiedCard(self):
        pass
    

    def test_addCustomCard(self):
        pass


    def test_listAllCards(self):
        pass

    def test_colourValue(self):
        pass

    def test__printMoveSet(self):
        pass
        
        


if __name__ =='__main__':
      
      unittest.main()