# TODO

from enum import Enum
import numpy as np
import types
from dataclasses import dataclass


@dataclass
class UnitBase:

    unit_name: str
    to_default_unit: types.LambdaType
    from_default_unit: types.LambdaType

    @classmethod
    def get_default_unit(self):
        return self.DEFAULT

    def is_default_unit(self):
        return self is self.DEFAULT

    def convert_to(self, value: float, to_unit: Enum) -> float:
        return to_unit.from_default_unit(self.to_default_unit(value))


class Angle(UnitBase, Enum):
    DEGREES = "deg", lambda u: u, lambda u: u
    RADIANS = "rad", lambda u: u * 180 / np.pi, lambda u: u * np.pi / 180
    ARCMINUTES = "arcmin", lambda u: u / 60, lambda u: u * 60
    ARCSECONDS = "arcsec", lambda u: u / 3600, lambda u: u * 3600

    DEFAULT = DEGREES


class Temperature(UnitBase, Enum):

    CELSIUS = "°C", lambda u: u, lambda u: u
    KELVIN = "K", lambda u: u - 273.15, lambda u: u + 273.15

    FARENHEIT = "°F", lambda u: (u - 32.0) * 5.0 / 9.0, lambda u: u * 9.0 / 5.0 + 32.0
    RANKINE = "R", lambda u: (u - 491.67) * 5.0 / 9.0, lambda u: u * 9.0 / 5.0 + 491.67

    DEFAULT = CELSIUS


class Distance(UnitBase, Enum):

    METERS = "m", lambda u: u, lambda u: u
    NANOMETERS = "nm", lambda u: u * 1e-9, lambda u: u / 1e-9
    MICROMETERS = "um", lambda u: u * 1e-6, lambda u: u / 1e-6
    MILLIMETERS = "mm", lambda u: u * 1e-3, lambda u: u / 1e-3
    CENTIMETERS = "cm", lambda u: u * 1e-2, lambda u: u / 1e-2
    KILOMETERS = "km", lambda u: u * 1e3, lambda u: u / 1e3

    FEET = "ft", lambda u: u * 0.3048, lambda u: u / 0.3048
    INCHES = "in", lambda u: u * 0.0254, lambda u: u / 0.0254
    YARDS = "yd", lambda u: u * 0.9144, lambda u: u / 0.9144
    MILES = "mi", lambda u: u * 1609.344, lambda u: u / 1609.344

    DEFAULT = METERS


class CompositeUnit(UnitBase):
    # TODO
    def __init__(self, composition) -> None:
        pass
