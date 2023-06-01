import os, sys
import unittest

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append(parentdir+'\\envs')
from envs.OnitamaWorld import OnitamaEnv
sys.path.append(parentdir+'\\GameEngine')
from GameEngine.Game import Game
from gymnasium import spaces

import numpy as np

# The kind of tests that one can do,
# Give it a particular state - know what next board state is -> compare this to what the board is supposed to be
# Can do this for a few cases -> Look at equivelance classes
     
#      E.g if we are looking at chess - lets test a move 
#                     taking another piece
#                     a board state one step away from winning -> arch -> king


class testEnv(unittest.TestCase):
     def __init__(self, methodName: str = "runTest") -> None:      
          super().__init__(methodName)
               
     def test_reset(self):

          envStub = DummyEnv()
          obs,info = envStub.reset(seed=None,options="10200010304424041434412345")
          expectedBoard = np.array(
                    [
                        [1] * 5,
                        [0] * 5,
                        [0] * 5,
                        [0] * 5,
                        [2] * 5,
                    ],
                    dtype=np.int32,
                )
            # need to place each piece 
          expectedcards = np.array([1,2])
          # Testing returned board
          self.assertTrue((expectedBoard == obs["Board"]).all())
          
          # Testing returned Cards
          self.assertEqual(expectedcards[0],obs["Cards"][0])
          self.assertEqual(expectedcards[1],obs["Cards"][1])

     def test_step(self):
          
          envStub = DummyEnv()
          obs,info = envStub.reset(seed=None,options="10200010304424041434412345")
          print("STEP TEST")
          action = {"piece" : 2,"move" : 5,"card" : 1}
          obs, reward, terminated, booL,info = envStub.step(action)
          expectedBoard = np.array([
                                   [1, 0, 1, 1, 1],
                                   [0, 1, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [2, 2, 2, 2, 2]
                                   ])
          self.assertTrue((expectedBoard == obs["Board"]).all())
          self.assertEqual(reward,0)

     def test_win(self):
          
          envStub = DummyEnv()
        
          obs,info = envStub.reset(seed=None,options="10200010304424041434412345")

          print("WIN TEST")
          envStub.game.makeMove(1,1,envStub.game.player2.pieces[0])
          action = {"piece" : 2,"move" : 5,"card" : 1}
          obs, reward, terminated, booL,info = envStub.step(action)



          expectedBoard = np.array([
                                   [1, 0, 1, 1, 1],
                                   [0, 1, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [2, 2, 0, 2, 2]
                                   ])
          self.assertTrue((expectedBoard == obs["Board"]).all())
          self.assertEqual(reward,100)
     def test_win(self):
          
          envStub = DummyEnv()
        
          obs,info = envStub.reset(seed=None,options="10200010304424041434412345")

          print("WIN TEST")
          action = {"piece" : 2,"move" : 4,"card" : 1}
          obs, reward, terminated, booL,info = envStub.step(action)
          expectedBoard = np.array([
                                   [1, 1, 1, 1, 1],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0],
                                   [2, 2, 2, 2, 2]
                                   ])
          self.assertTrue((expectedBoard == obs["Board"]).all())
          self.assertEqual(reward,-10)



class DummyEnv(OnitamaEnv):
     def __init__(self,
                 render_mode=None, 
                 ):
        self._currentPlayer = 1
        self.game = Game("10200010304424041434412345")
        # creating dictionary to correlate discrete value to a piece object
        #Player 1 pieces
        self.player1Pieces:dict = {}
        for x in range(len(self.game.player1.pieces)):
             self.player1Pieces[x] = self.game.player1.pieces[x]
        #Player 2 pieces
        self.player2Pieces:dict = {}
        for x in range(len(self.game.player2.pieces)):
             self.player2Pieces[x] = self.game.player2.pieces[x]
        
        # make it also return cards available
        self.observation_space = spaces.Dict(
            {
            "Board":spaces.Box(-5, 5, (5,5), dtype=int),
            "Cards":spaces.MultiDiscrete([16,16,16,16,16])
            }
        )
        # We have many actions, select card, select move, select piece
        self.action_space = spaces.Dict(
            {
            "piece": spaces.Discrete(5),
            "move": spaces.Discrete(25),
            "card": spaces.Discrete(16)
            }
        )   
    

if __name__ =='__main__':
      
      unittest.main()

