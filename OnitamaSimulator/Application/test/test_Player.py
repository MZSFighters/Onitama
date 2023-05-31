import os, sys
import unittest
from IPython.utils.capture import capture_output

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from GameEngine.Player import Player
from GameEngine.Game import Game

class TestPiece(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")
    def setUp(self):
        print("\nRunning setUp method...")
        self.player_1 = Player("player1", True)
        self.player_2 = Player("player2", False)

    def tearDown(self):
        print("Running tearDown method...")


    #testing test_colour method
    def test_getColour(self):
        print("Running test_colour...")
        game = Game()
        self.assertEqual(self.player_1.getColour(), "Red")
        self.assertEqual(self.player_2.getColour(), "Blue")

    def test_printPieces(self):
         print("Running test_printPieces...")
         game = Game()

         with capture_output() as c:
            game.player1.PrintPieces()
         c()
         self.assertIsNotNone(c.stdout)
   
    @classmethod
    def tearDownClass(cls):
            print("\ntearDownClass method: Runs after all tests...")
            

if __name__=='__main__':
        unittest.main()
