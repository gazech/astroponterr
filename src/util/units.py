# TODO

from enum import Enum
import numpy as np
import types
from dataclasses import dataclass


@dataclass
class UnitBase():

    unitName: str
    toDefaultUnit: types.LambdaType
    fromDefaultUnit: types.LambdaType

    @classmethod
    def getDefaultUnit(self):
        return self.DEFAULT
    
    def isDefaultUnit(self):
        return self is self.DEFAULT
    
    def convert(self, value: float, toUnit: Enum) -> float:
        return toUnit.fromDefaultUnit( self.toDefaultUnit(value) )


class Angle(UnitBase, Enum):
    DEGREES = 'deg',       lambda u: u,              lambda u: u
    RADIANS = 'rad',       lambda u: u * np.pi/180,  lambda u: u * 180/np.pi 
    ARCMINUTES = 'arcmin', lambda u: u / 60,         lambda u: u * 60
    ARCSECONDS = 'arcsec', lambda u: u / 3600,       lambda u: u * 3600

    DEFAULT = DEGREES
 

# class Temperature(UnitBase, Enum):

#     CELSIUS = '°C'
#     KELVIN = 'K'

#     FARENHEIT = '°F'
#     RANKINE = 'R'

#     DEFAULT = CELSIUS


class Distance(UnitBase, Enum):

    METERS      = 'm',  lambda u: u     , lambda u: u  
    NANOMETERS  = 'nm', lambda u: u*1e-9, lambda u: u/1e-9       
    MICROMETERS = 'um', lambda u: u*1e-6, lambda u: u/1e-6       
    MILLIMETERS = 'mm', lambda u: u*1e-3, lambda u: u/1e-3       
    CENTIMETERS = 'cm', lambda u: u*1e-2, lambda u: u/1e-2       
    KILOMETERS  = 'km', lambda u: u*1e+3, lambda u: u/1e+3       

    FEET   = 'feet'  , lambda u: u, lambda u: u      
    INCHES = 'inches', lambda u: u, lambda u: u        
    YARDS  = 'yards' , lambda u: u, lambda u: u       
    MILES  = 'miles' , lambda u: u, lambda u: u       

    DEFAULT = METERS

        
class CompositeUnit(composition,*units):
    # TODO
    def __init__(self) -> None:
        pass