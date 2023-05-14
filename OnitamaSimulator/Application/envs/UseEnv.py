from gymnasium.envs.registration import register
import gymnasium as gym

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
            action = env.action_space.sample()  # agent policy that uses the observation and info
            observation, reward, terminated, truncated, info = env.step(action)

            if terminated or truncated:
                observation, info = env.reset()

env =UseEnv()
env.DoTheEnv()