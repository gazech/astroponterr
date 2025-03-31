# TODO: interface for astrometry.net (or other solver)

from abc import ABC, abstractmethod
from enum import StrEnum
from pathlib import Path
from typing import Annotated, Literal, TypeVar

import numpy as np
from astropy.io import fits

PixelType = TypeVar("PixelType", bound=np.generic)
ImageArrayType = Annotated[np.typing.NDArray[PixelType], Literal["N", "N"]]

class SolverType(StrEnum):
    """
    Enum for the different solver types.
    """
    ASTROMETRY_NET = "astrometry.net"


class Solver(ABC):
    """
    Abstract base class for all astrometric solvers. See SolverType for available solvers.
    """

    _solution = None
    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, _):
        raise AttributeError(f"Solution for {type(self)} is read-only.")

    _memory_mapping = True
    @property
    def use_memmory_mapping(self):
        return self._memory_mapping

    @use_memmory_mapping.setter
    def use_memmory_mapping(self, flag: bool):
        if not isinstance(flag, bool):
            raise ValueError("use_memmory_mapping must be a boolean.")
        self._memory_mapping = flag

    @property
    @abstractmethod
    def solver(self) -> SolverType:
        pass

    @solver.setter
    def solver(self, _):
        raise AttributeError(f"Solver type for {type(self)} is read-only.")

    @abstractmethod
    def _solve(self, image: ImageArrayType):
        pass

    def solve(self, fits_path: Path):
        """
        Solve the FITS image using the specified solver.
        """
        with fits.open(fits_path,mode="readonly",memmap=self._memory_mapping) as hdul:
            image_data = hdul[0].data
        self._solve(image=image_data)


class AstrometrySolver(Solver):
    """
    Astrometry solver using astrometry.net.
    """

    def __init__(self):
        super().__init__()
        self._solver = SolverType.ASTROMETRY_NET

    def _solve(self, image: ImageArrayType):
        pass

    @property
    def solver(self) -> SolverType:
        return self._solver

