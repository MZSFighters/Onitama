import os, sys
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)



from GameEngine.Player import Player

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
    def test_color(self):
        print("Running test_colour...")
        self.assertEqual(self.player_1.color(), "Red")
        self.assertEqual(self.player_2.color(), "Blue")

    def test_printPieces(self):
         print("Running test_printPieces...")
         pass
   
    @classmethod
    def tearDownClass(cls):
            print("\ntearDownClass method: Runs after all tests...")
            

if __name__=='__main__':
        unittest.main()