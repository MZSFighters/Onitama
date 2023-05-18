import numpy as np
import gymnasium as gym
from gymnasium import spaces
from gymnasium.spaces import Box

import sys
sys.path[0] =sys.path[0] + ('\../')
from GameEngine import *



DEFAULT_BOARD = np.array(
    [
        [-1, -2, -3, -4, -5],
        [0] * 5,
        [0] * 5,
        [0] * 5,
        [1, 2, 3, 4, 5],
    ],
    dtype=np.int32,
)

DEFAULT_MOVES = np.array(
     [0,0],
     [0,-1],
     [0,-2],
     [0,1],
     [0,2],
     [1,0],
     [1,-1],
     [1,-2],
     [1,1],
     [1,2],
     [2,0],
     [2,-1],
     [2,-2],
     [2,1],
     [2,2],
     [-1,0],
     [-1,-1],
     [-1,-2],
     [-1,1],
     [-1,2],
     [-2,0],
     [-2,-1],
     [-2,-2],
     [-2,1],
     [-2,2]
)
DEFAULT_CARDS = np.array( 
        (Card( 'Tiger', True, [[-1,0], [2, 0]])) ,
        (Card( 'Crab', True, [[1,0], [0, 2], [0, -2]])) ,
        (Card( 'Monkey', True, [[1,-1], [1, 1], [-1, 1], [-1,-1]])) ,
        (Card( 'Crane', True, [[1,0], [-1, -1], [-1, 1]])), 
        (Card( 'Dragon', False, [[-1,-1], [-1, 1], [1, -2], [1, -2]] )),
        (Card( 'Elephant', False, [[0,1], [0, -1], [1,-1], [1, 1] ])) ,
        (Card( 'Mantis', False, [[-1,0], [1,-1], [1, 1] ]))  ,
        (Card( 'Boar', False, [[0,-1], [0, 1], [1, 0] ])) ,    
        (Card( 'Frog', False, [[1,1], [-1, -1], [0,2] ])),
        (Card( 'Goose', True, [[0,1], [0, -1], [-1,-1], [1,1] ])),  
        (Card( 'Horse', False, [[1,0], [-1, 0], [0,1] ])), 
        (Card( 'Eel', True, [[-1,1], [1, 1], [0,-1] ])),   
        (Card( 'Rabbit', True, [[-1,1], [1, -1], [0,-2] ])) ,
        (Card( 'Rooster', False, [[0,-1], [1, -1], [0,1], [-1,1] ])),
        (Card( 'Ox', True, [[-1,0], [1, 0], [0,-1] ])),
        (Card( 'Cobra', False, [[0,1], [1, -1], [-1,-1] ]))        
)
# ONITAMA GYM ENVIRONMENT CLASS
# ---------------------------
class OnitamaEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self,
                 render_mode=None, 

                 
                 ):
        self._currentPlayer = 1
        self.game = Game()

        # make it also return cards available
        self.observation_space = spaces.Box(-5, 5, (5,5), dtype=int)
        # We have many actions, select card, select move, 
        self.action_space = spaces.Dict(
            {
            "piece": spaces.Discrete(5),
            "move": spaces.Discrete( 25, start=1)
            }
        )   

    def get_card(self, card:int):
         return(DEFAULT_CARDS[card])         
    def get_action(self, action:int):
         return DEFAULT_MOVES[action]
         

    def get_info(self):
        return{
            "temp":None
        }

    def get_obs(self):
            return self._board
    
    def reset(self, seed = None, options = None):
        super().reset(seed = seed)
        self._board = DEFAULT_BOARD
        self._currentPlayer = 1


        self.game = Game()
        
        info = self.get_info()
        obs = self.get_obs()
        return obs,info

    def step(self, action):
        # action - card and a move
        # action space will need to return a move then we need to calculate the position of said move from the piece
        # move -> place

        if (self._currentPlayer == 1):
             player:Player = self.game.player1
        else:
             player:Player = self.game.player2
        move = self.get_action(action["move"])
        card:Card = self.get_card(action["card"])
        #AImakeTurn(self, player,  piece, card, move)
        self.game.AImakeTurn(player,1,card,move)
        # reward
        reward = 0
        # termination
        terminated = False
        # return
        info = self.get_info()
        obs = self.get_obs()
        return obs, reward, terminated, False,info

    def MovePiece(self,piece,place):
        pass

    def printBoard(self):
        print(self._board)
        print(type(self._board))