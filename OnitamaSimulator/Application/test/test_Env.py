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
        obs,info = envStub.reset("10200010304424041434412345")
        self.assertIsNotNone(obs)
        self.assertIsNotNone(info)

    def test_step(self):
        envStub = DummyEnv()
        obs,info = envStub.reset("10200010304424041434412345")
        action = {"piece" : 1,"move" : 0,"card" : 0}

        obs, reward, terminated, booL,info = envStub.step(action)

        self.assertIsNotNone(obs)
        self.assertIsNotNone(reward)
        self.assertIsNotNone(terminated)
        self.assertEqual(booL,False)
        self.assertIsNotNone(info)

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
        self.observation_space = spaces.Box(-5, 5, (5,5), dtype=int)
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

