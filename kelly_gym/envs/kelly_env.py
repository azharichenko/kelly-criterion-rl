import gym
from gym import spaces
from gym import utils
from gym.utils import seeding, EzPickle
import numpy as np

from random import randint

import plotly.graph_objects as go

import logging
logger = logging.getLogger(__name__)

class KellyEnv(gym.Env, EzPickle):
  metadata = {'render.modes': ['human']}

  def __init__(self, starting_capital: float=25.0, prob: float=0.6):
    self.action_space = spaces.Tuple([
            spaces.Discrete(2),
            spaces.Box(low=0.01, high=0.99, shape=(1,))
    ])
    self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0]),
            high=np.array([np.Inf, 1.0]),
            dtype=np.float32
    )

    self.starting_capital = 25.0
    self.capital = self.starting_capital
    self.heads_probability = prob
    self.history = [self.starting_capital]
    self.i = 1

  def reset(self):
    self.capital = self.starting_capital
    self.history = [self.starting_capital]
    self.i = 1
    return [self.capital, self.heads_probability]

  def step(self, action):
    done: bool = False
    reward: int = 0
    head, prop = action
    bet = round(prop[0] * self.capital, 2)
    cap = self.capital
    self.i += 1

    if head == np.random.choice([0, 1], 1, p=[1-self.heads_probability, self.heads_probability]):
      self.capital += bet 
      reward = 1 + np.log(self.i) + np.log(self.capital)
    else:
      self.capital -= bet
      reward = -1 - np.log(self.i) - np.log(self.capital)

    if bet == 0 or bet == cap:
      reward = -10

    self.capital = round(self.capital, 2)
    self.history.append(self.capital)

    if  self.capital <= 0:
      done = True

    return [self.capital, self.heads_probability], reward, done, {}

  def render(self, mode='human'):
    indexes = np.arange(len(self.history))
    fig = go.Figure(data=go.Scatter(x=indexes, y=self.history))
    fig.show()

#   def close(self):
#     ...
