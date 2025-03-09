"""Attitude Class"""

from collections import namedtuple
from dataclasses import dataclass

Vector2D = namedtuple("Vector2D", ["x", "y", "units"])


@dataclass
class Collection(object):
    pass


class Camera(object):
    def __init__(self):
        self._fov = Vector2D
        self._pix_pitch = Vector2D
        self._pix_dimensions = Vector2D
        self._exp_time = None
        self._frame_rate = None
        self._fpa_temp = None
        return

    def __repr__(self):
        return

    @property
    def field_of_view(self):
        """Degrees"""
        return

    @property
    def pixel_pitch(self):
        """m per pixel"""
        return

    @property
    def pixel_dimensions(self):
        """Pixels"""
        return

    @property
    def exposure_time(self):
        """configured exposure time"""
        return

    @property
    def frame_rate(self):
        """camera frame rate"""
        return

    @property
    def fpa_temperature(self):
        """FPA temp"""
        return

    def calibrate(self):
        """dark/bias/flat"""
        return

    def capture(self):
        """trigger camera"""
        return
