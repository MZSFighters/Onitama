import numpy as np
import gymnasium as gym
from gymnasium import spaces
from gymnasium.spaces import Box

import sys
sys.path[0] =sys.path[0] + ('\../')
from GameEngine import *

DEFAULT_REWARDS = dict({
    "Player 1 Win": 100,
    "Player 2 Win": 100,
    "Take piece": 20,
    "Incorrect Action":-10
})

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
        (Card( 'Tiger', True, [[-1,0], [2, 0]])),
        (Card( 'Crab', True, [[1,0], [0, 2], [0, -2]])),
        (Card( 'Monkey', True, [[1,-1], [1, 1], [-1, 1], [-1,-1]])),
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
        # creating dictionary to correlate discrete value to a piece object
        #Player 1 pieces
        self.player1Pieces:dict
        for x in range(len(self.game.player1.pieces)):
             self._player1Pieces[x] = self.game.player1.pieces[x]
        #Player 2 pieces
        self.player2Pieces:dict
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

    # Space Converters
    def get_card(self, card:int):
        # return the appropriate card and validate said card
        selectedCard = DEFAULT_CARDS[card]
        if(self._currentPlayer ==1):
            if selectedCard in self.game.player1.cards:
                return selectedCard
            else:
                return None
        if(self._currentPlayer ==2):
            if selectedCard in self.game.player2.cards:
                return selectedCard
            else:
                return None   
        
    def get_move(self, action:int):
        return DEFAULT_MOVES[action]
    
    def get_piece(self, piece:int):
         # we recieve an integer
         # use the piece dictionaries to return the correct piece object refrence
         # Return none if the piece is ded
        if (self._currentPlayer == 1):
            selectedPiece = self.player1Pieces[piece]
            if(piece.row != -1):
                return selectedPiece
            else:
                return None

        if (self._currentPlayer == 2):
            selectedPiece = self.player2Pieces[piece]
            if(piece.row != -1):
                return selectedPiece
            else:
                return None
        

    def get_info(self):
        return{
            "temp":None
        }

    def get_obs(self):
            #self.game.board -> int board 
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

        # Set current Player
        if (self._currentPlayer == 1):
             player:Player = self.game.player1
        else:
             player:Player = self.game.player2
        
        #Get move, piece and card
        move = self.get_move(action["move"])
        card:Card = self.get_card(action["card"])
        piece:Piece = self.get_piece(action["piece"]) 

        #init reward at 0
        reward = 0

        # Is the card and piece valid?
        if (piece == None or card == None ):
            reward = DEFAULT_REWARDS("Incorrect Action")
        else:   
            #AImakeTurn(self, player,  piece, card, move)
            turnReward = self.game.AImakeTurn(player,piece,card,move)

            if (turnReward == 3):
                reward = DEFAULT_REWARDS("Incorrect Acion")
            elif(turnReward == 1 or turnReward == 2):
                reward = DEFAULT_REWARDS("Player 1 Wins")
        
        # termination if someone won or if an invalid move was chosen
        if(reward ==DEFAULT_REWARDS("Player 1 Wins") or reward<0):
            terminated = True
        else:
            terminated = False

        info = self.get_info()
        obs = self.get_obs()

        #Switch Players
        if(self._currentPlayer == 1):
            self._currentPlayer = 2
        else:
            self._currentPlayer = 1


        return obs, reward, terminated, False, info

    def MovePiece(self,piece,place):
        pass

    def printBoard(self):
        print(self._board)
        print(type(self._board))