import ray
from ray.rllib import dqn
import time

ray.init()
agent = dqn.DQNAgent(env='CartPole-v0', config={'num_workers':2})

time.sleep(30)
