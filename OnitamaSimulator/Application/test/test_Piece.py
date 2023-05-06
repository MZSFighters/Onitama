import os, sys
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

#import GameEngine.Piece as Piece
from GameEngine.Piece import Piece

class TestPiece(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")
    def setUp(self):
        print("\nRunning setUp method...")
        self.piece_1 = Piece(True,False,1,2)
        self.piece_2 = Piece(False,True,0,3)

    def tearDown(self):
        print("Running tearDown method...")

    #testing test_colour method
    def test_colour(self):
        print("Running test_colour...")
        self.assertEqual(self.piece_1.stringColour(), "Red")
        self.assertEqual(self.piece_2.stringColour(), "Blue")

    # Not using setTile class right now :)
    # def test_setTile(self, tile):

    @classmethod
    def tearDownClass(cls):
            print("\ntearDownClass method: Runs after all tests...")
            

if __name__=='__main__':
        unittest.main()