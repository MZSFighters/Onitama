import os, sys
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

#import GameEngine.Tile as Tile
#import GameEngine.Piece as Piece
from GameEngine.Tile import Tile
from GameEngine.Piece import Piece

class TestPiece(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")
    def setUp(self):
        print("\nRunning setUp method...")
        self.piece_1 = Piece(True,False,1,2)        # piece.colour is RED
        self.piece_2 = Piece(False,True,0,3)        # piece.colour is BLUE
        self.piece_3 = None
        self.tile_1 = Tile(self.piece_1, 0, 2)
        self.tile_2 = Tile(self.piece_2, 0, 3)
        self.tile_3 = Tile(self.piece_3, 0, 1)
    def tearDown(self):
        print("Running tearDown method...")

# Testing if the tile is a master seat or not depending on the coordinates of the tile
    def test_isMasterSeat(self):
         print("Running test_isMasterSeat...")
         self.assertEqual(self.tile_1.isMasterSeat(), True)
         self.assertEqual(self.tile_2.isMasterSeat(), False)
         self.assertEqual(self.tile_3.isMasterSeat(), False)


# Testing the Value() which assigns a value to a piece depending on their location on the board
    def test_Value(self):
         print("Running test_Value...")
         self.assertEqual(self.tile_1.Value(), 1)       # Checking if RED is indeed value = 1
         self.assertEqual(self.tile_2.Value(), 2)       # Checking if BLUE is indeed value = 1
         self.assertEqual(self.tile_3.Value(), 0)       # No piece so value = 0


    @classmethod
    def tearDownClass(cls):
            print("\ntearDownClass method: Runs after all tests...")

if __name__=='__main__':
        unittest.main()
            