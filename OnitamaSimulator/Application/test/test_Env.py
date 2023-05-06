import os, sys
import unittest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append(parentdir+'\\envs')
from envs.OnitamaWorld import OnitamaEnv

import numpy as np

DEFAULT_BOARD_STATE = np.array(
    [
        [-1, -2, -3, -4, -5],
        [0] * 5,
        [0] * 5,
        [0] * 5,
        [1, 2, 3, 4, 5],
    ],
    dtype=np.int32,
)


class testEnv(unittest.TestCase):
    def test_reset(self):
        envStub = OnitamaEnv()
        obs,info = envStub.reset()
        self.assertTrue((obs-DEFAULT_BOARD_STATE).all)
        self.assertEqual(info,{"temp" : None})

    def test_step(self):
        envStub = OnitamaEnv()
        action = {"piece" : 1,"move" : 0}
        obs, reward, terminated, booL,info = envStub.step(action)
        self.assertTrue((obs-DEFAULT_BOARD_STATE).all)
        self.assertEqual(reward,0)
        self.assertEqual(terminated, False)
        self.assertEqual(booL,False)
        self.assertEqual(info,{"temp" : None})

if __name__ =='__main__':
      
      unittest.main()
