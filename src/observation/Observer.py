"""Observer Class"""

from uuid import uuid4
from Observation import Observation


class Observer(object):

    def __init__(self):
        self.obs_dict = {}
        self.id = uuid4()
        return

    def __repr__(self):
        return f"I am an observer with ID {self.id:s}; {len(self.obs_dict)} observations total"

    def get_observer_id(self):
        return f"My super special observer ID is {self.observer_id:s}"

    def add_observation(self, obs: Observation):
        return self.obs_dict.update({uuid4(): obs})
