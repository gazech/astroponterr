"""Position/Attitude Class"""

import numpy as np
from scipy.spatial.transform import Rotation
from util.enums import ReferenceFrame


class State(object):

    def __init__(
        self,
        rf: ReferenceFrame = ReferenceFrame.UNDETERMINED,
        pos: np.ndarray = np.array([0, 0, 0]),
        att: np.ndarray = Rotation,
    ):
        self._reference_frame = rf
        return

    def __repr__(self):
        return

    @property
    def reference_frame(self):
        return self._reference_frame

    @property
    def position(self) -> np.nparray:
        return self._position

    @property
    def attitude(self) -> np.nparray:
        return self._attitude
