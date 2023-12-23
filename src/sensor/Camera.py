"""Attitude Class"""

import numpy as np
from collections import namedtuple

Vector2D = namedtuple('Vector2D',['x','y','units'])

class Camera(object):
    
    def __init__(self):
        self._fov = Vector2D(None,None,)
        self._pixPitch = Vector2D
        self._pixDim = Vector2D
        return
    
    def __repr__(self):
        return
    
    @property
    def fieldOfView(self):
        """Degrees"""
        return
    
    @property
    def pixelPitch(self):
        """Degress per pixel"""
        return
    
    @property
    def pixelCount(self):
        """Pixels"""
        return
    
    @property
    def exposureTime(self):
        """configured exposure time"""
        return
    
    @property
    def temperature(self):
        """FPA temp"""
        return
    
    def calibrate(self):
        """dark/bias/flat"""
        return
    
    def capture(self):
        """trigger camera"""
        return

