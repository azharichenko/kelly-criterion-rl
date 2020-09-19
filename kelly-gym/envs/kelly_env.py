import gym
from gym import spaces
from gym import utils
from gym.utils import seeding
import numpy as np

import logging
logger = logging.getLogger(__name__)

class KellyEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self, starting_capital):
    self.observation_space = spaces.Box(low=0.0)
    self.action_space = spaces.Tuple(
            spaces.Discrete(2),
            spaces.Box(low=0.0, high=1.0),
    )
    self.starting_capital = starting_capital
    self.capital = starting_capital


  def reset(self):
    self.capital = self.starting_capital


  def _outcome(self):
      return

#   def render(self, mode='human'):
#     ...

#   def close(self):
#     ...
