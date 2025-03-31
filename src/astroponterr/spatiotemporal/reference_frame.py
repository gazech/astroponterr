from enum import Enum
from astropy.coordinates import ITRS, ICRS, BaseCoordinateFrame

# subset of desired coordinate frames to work with (mostly just a map to astropy at this moment)
class ReferenceFrameType(Enum):
    ICRS = ICRS
    ITRS = ITRS
