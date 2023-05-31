from gymnasium.envs.registration import register
import gymnasium as gym
'''
 self.action_space = spaces.Dict(
            {
            "piece": spaces.Discrete(5),
            "move": spaces.Discrete(25),
            "card": spaces.Discrete(16)
            }
        )   

'''
class UseEnv():
    def __init__(self) -> None:
        pass

    def DoTheEnv(self):
        register(
            id = 'OnitamaEnv-v0',
            entry_point='envs:OnitamaEnv',
            max_episode_steps=2000
        )
        env = gym.make('OnitamaEnv-v0')
        observation, info = env.reset()
        for _ in range(10):
            '''
            Notes - could use if statements to check what to reward each agent. 
                - Only do learning after the pair make an action.
                - 
            '''
            # agent 0
            action = env.action_space.sample(mask={"piece":info["pieceMask"],"move":info["moveMask"],"card":info["cardMask"]})  # agent policy that uses the observation and info
            observation, reward, terminated, truncated, info = env.step(action)
            
            if terminated or truncated:
                observation, info = env.reset()

