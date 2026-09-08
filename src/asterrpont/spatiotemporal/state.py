"""Position/Attitude Class"""

import dataclasses

from astropy.time import Time
from astropy.units import Quantity, meter, second
from scipy.spatial.transform import Rotation

from asterrpont.spatiotemporal.reference_frame import ReferenceFrameType


@dataclasses.dataclass
class State(object):
    attitude: Rotation = None
    position: Quantity[meter] = None  # is this the right class?
    velocity: Quantity[meter / second] = None
    acceleration: Quantity[meter / (second**2)] = None
    reference_frame: ReferenceFrameType = None
    time: Time = None
