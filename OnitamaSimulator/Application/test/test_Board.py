import os, sys
import unittest
from IPython.utils.capture import capture_output

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from GameEngine.Game import Game
from GameEngine.Board import Board
from GameEngine.Player import Player

class TestPiece(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")
    def setUp(self):
        print("\nRunning setUp method...")
        self.player_1 = Player("player1", True)
        self.player_2 = Player("player2", False)
        self.board = Board(self.player_1, self.player_2)

    def tearDown(self):
        print("Running tearDown method...")

    # testing test_returnTile method
    def test_returnTile(self):
        print("Running test_returnTile...")
        # testing different coordinates for tiles...
        self.assertEqual(self.board.arr[0][0], self.board.returnTile(0, 0))
        self.assertEqual(self.board.arr[4][4], self.board.returnTile(4, 4))
        self.assertEqual(self.board.arr[1][4], self.board.returnTile(1, 4))
        self.assertEqual(self.board.arr[4][1], self.board.returnTile(4, 1))
        

    def test_printBoard(self):
         print("Running test_printBoard...")
         game = Game()

         with capture_output() as c:
            game.board.printBoard()

         c()
         self.assertIsNotNone(c.stdout)

 

    @classmethod
    def tearDownClass(cls):
            print("\ntearDownClass method: Runs after all tests...")
            

if __name__=='__main__':
        unittest.main()