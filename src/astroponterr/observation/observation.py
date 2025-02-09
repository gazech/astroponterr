"""Observation Class"""

# TODO: make into dataclass fr

from dataclasses import dataclass
from datetime import datetime

from astroponterr.sensor.camera import Collection
from astroponterr.spatiotemporal.state import State


@dataclass
class Observation(object):

    time_of_observation: datetime
    state: State
    camera_data: Collection
