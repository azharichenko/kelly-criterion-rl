
import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Kelly-v0',
    entry_point='kelly-gym.envs:InventoryEnv',
    timestep_limit=100,
    reward_threshold=1.0,
    nondeterministic = True,
)