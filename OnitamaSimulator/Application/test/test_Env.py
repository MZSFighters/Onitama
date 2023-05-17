import os, sys
import unittest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append(parentdir+'\\envs')
from envs.OnitamaWorld import OnitamaEnv

import numpy as np




class testEnv(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:      
         super().__init__(methodName)
            



    def test_reset(self):
        envStub = OnitamaEnv()
        obs,info = envStub.reset()
        self.assertIsNotNone(obs)
        self.assertIsNotNone(info)

    def test_step(self):
        envStub = OnitamaEnv()
        obs,info = envStub.reset()
        action = {"piece" : 1,"move" : 0,"card" : 0}
        obs, reward, terminated, booL,info = envStub.step(action)
        self.assertIsNotNone(obs)
        self.assertIsNotNone(reward)
        self.assertIsNotNone(terminated)
        self.assertEqual(booL,False)
        self.assertIsNotNone(info)

if __name__ =='__main__':
      
      unittest.main()
