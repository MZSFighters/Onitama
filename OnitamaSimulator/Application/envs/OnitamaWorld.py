import numpy as np
import gymnasium as gym
from gymnasium import spaces
from gymnasium.spaces import Box

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

# ONITAMA GYM ENVIRONMENT CLASS
# ---------------------------
class OnitamaEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self,
                 render_mode=None, 
                 initial_board = DEFAULT_BOARD,
                 
                 ):
        self._board = DEFAULT_BOARD
        self._currentPlayer = 1

        # make it also return cards available
        self.observation_space = spaces.Box(-5, 5, (5,5), dtype=int)
        # We have many actions, select card, select move, 
        self.action_space = spaces.Dict(
            {
            "piece": spaces.Discrete(5),
            "move": spaces.Discrete( 25, start=1)
            }
        )   

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
        info = self.get_info()
        obs = self.get_obs()
        return obs,info

    def step(self, action):
        # action
        piece = action["piece"]
        move = action["move"]
        piece *= self._currentPlayer
        print(piece)
        self.MovePiece(piece,move)
        self._currentPlayer =-1*self._currentPlayer
        # reward
        reward = 0
        # termination
        terminated = False
        # return
        info = self.get_info()
        obs = self.get_obs()
        return obs, reward, terminated, False,info

    def MovePiece(self,piece,place):
        counter=0
        for i in range(5):
            for i2 in range(5):
                if (self._board[i][i2] == piece):
                    self._board[i][i2] = 0
                counter += 1
                if(counter == place):
                    self._board[i][i2] = piece
        self.printBoard()

    def printBoard(self):
        print(self._board)
        print(type(self._board))