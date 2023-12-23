"""Observation Class"""

# TODO: make into dataclass fr

import numpy as np
from dataclasses import dataclass
from datetime import datetime
from util.enums import ReferenceFrame
from sensor import Camera
from spatiotemporal import Position, Attitude

@dataclass
class Observation(object):

    timeOfObservation: datetime
    location: Position
    attitude: Attitude
    referenceFrame: ReferenceFrame
    cameraData: Camera
    
