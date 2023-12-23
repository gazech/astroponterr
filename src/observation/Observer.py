"""Observer Class"""

from uuid import uuid4
from Observation import Observation

class Observer(object):
    
    def __init__(self):
        self.obsDict = {}
        self.id = uuid4()
        return
    
    def __repr__(self):
        return f"I am an observer with ID {self.id:s}; {len(self.obsDict)} observations total"
    
    def getObserverID(self):
        return f"My super special observer ID is {self.observerID:s}"
    
    def addObservation(self, obs: Observation):
        return self.obsDict.update({uuid4():obs})

