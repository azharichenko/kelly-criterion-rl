import gym
import kelly_gym

env = gym.make("Kelly-v0", starting_capital=50.0, prob=0.65)

# Random Agent
for i_episode in range(1):
    observation = env.reset()
    for t in range(1000):
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print(action, observation, reward, done, info) 
        if done:
            break