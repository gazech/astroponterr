# TODO: interface for astrometry.net (or other solver)

import tempfile
from abc import ABC, abstractmethod
from enum import StrEnum
from pathlib import Path
from typing import Annotated, Literal, TypeVar

import astrometry
import numpy as np
from astropy.io import fits

from astroponterr.logging.scribe import Scribe

logger = Scribe(__name__)

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

    For now, we'll use the python 'astrometry' package for prototyping.
    I'd like to use a custom wrapper in the future for use of local indeces.

    see: https://astrometry.net/doc/readme.html#getting-index-files for scales
    """

    def __init__(self, index_catalog: astrometry.Series):
        super().__init__()
        self._solver = SolverType.ASTROMETRY_NET
        self._cache_dir = None

    def _solve(self, image: ImageArrayType):

        logger.info(f"Using cache directory: {self._cache_dir}")

        # indexer = astrometry.series_4100.index_files(
        #     scales=set(range(7,20)),
        #     cache_directory=self._cache_dir,
        # )

        indexer = astrometry.series_5200.index_files(
            cache_directory=self._cache_dir,
            scales={6},
        )

        with astrometry.Solver(indexer)as solver:

            #FIXME tmp
            stars = [
                [388.9140568247906, 656.5003281719216],
                [732.9210858972549, 473.66395545775106],
                [401.03459504299843, 253.788113189415],
                [312.6591868096163, 624.7527729425295],
                [694.6844564647456, 606.8371776658344],
                [741.7233477959561, 344.41284826261443],
                [867.3574610200455, 672.014835980283],
                [1063.546651153479, 593.7844603550848],
                [286.69070190952704, 422.170016812049],
                [401.12779619355155, 16.13543616977013],
                [205.12103484692776, 698.1847350789413],
                [202.88444768690894, 111.24830187635557],
                [339.1627757703069, 86.60739435924549],
            ]

            self._solution = solver.solve(
                stars=stars,
                size_hint=None,
                position_hint=None,
                solution_parameters=astrometry.SolutionParameters(solve_id="testy"),
            )

            # pass 


    @property
    def solver(self) -> SolverType:
        return self._solver

