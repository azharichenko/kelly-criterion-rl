
import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Kelly-v0',
    entry_point='kelly_gym.envs:KellyEnv',
    max_episode_steps=1000,
)
