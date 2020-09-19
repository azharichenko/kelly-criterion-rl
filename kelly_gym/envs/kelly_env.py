import gym
from gym import spaces
from gym import utils
from gym.utils import seeding
import numpy as np

from random import randint

import logging
logger = logging.getLogger(__name__)

class KellyEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self, starting_capital: float=25.0, prob: float=0.6):
    self.action_space = spaces.Tuple([
            spaces.Discrete(2),
            spaces.Box(low=0.0001, high=1.0, shape=(1,))
    ])
    self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0]),
            high=np.array([255.0, 1.0]),
            dtype=np.float32
    )

    self.starting_capital = starting_capital
    self.capital = starting_capital
    self.heads_probability = prob

  def reset(self):
    self.capital = self.starting_capital
    return [self.capital, self.heads_probability]

  def step(self, action):
    done: bool = False
    reward: int
    head, prop = action
    bet = prop[0] * self.capital

    if head == np.random.choice([0, 1], 1, p=[1-self.heads_probability, self.heads_probability]):
      self.capital += bet
      reward = 1
    else:
      self.capital -= bet
      reward = -1

    self.capital = round(self.capital, 2)

    if  self.capital <= 0:
      done = True

    return [self.capital, self.heads_probability], reward, done, {}

#   def render(self, mode='human'):
#     ...

#   def close(self):
#     ...
