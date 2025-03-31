"""
Some precanned indeces for solving
"""

import tempfile
from pathlib import Path

import astrometry

from astroponterr.logging.scribe import Scribe

logger = Scribe(__name__)


DEFAULT_CACHE_PREFIX = "astrometry_cache/"

def _sanitize_path(path: str | Path) -> Path:
    """
    Sanitizes the path to a Path object.
    """
    if not path:
        return None
    elif isinstance(path, str):
        path = Path(path)
    elif not isinstance(path, Path):
        raise ValueError(f"Path must be a string or Path object, not {type(path)}")
    return path

class CatalogCacher:
    """
    Caches the astrometry.net catalogs for use in solving.
    """

    def __init__(self, cache_path: Path | None = None):

        self._cache_path = None
        input_cache_path = _sanitize_path(cache_path)

        if input_cache_path is None:
            logger.info("No cache directory provided, creating a new cache directory.")
            self.cache_path = Path(tempfile.mkdtemp(prefix=DEFAULT_CACHE_PREFIX))
        elif not input_cache_path.exists():
            logger.warning(f"No cache directory found for {input_cache_path.resolve()}.")
        else:
            logger.info(f"Using existing, supplied cache directory at {input_cache_path.resolve()}")
            self.cache_path = input_cache_path

    def __repr__(self):
        if self._cache_path:
            return f"{__name__}.CatalogCacher with cache at {self.cache_path.resolve()}"
        else:
            return f"{__name__}.CatalogCacher with no cache"

    @property
    def cache_path(self) -> Path:
        if not self._cache_path:
            logger.warning("No cache directory.")
        return self._cache_path

    @cache_path.setter
    def cache_path(self, path: Path):

        self._cache_path = _sanitize_path(path)

        if not self._cache_path.exists():
            logger.warning(f"Provided cache directory does not exist: {self._cache_path.resolve()}. Consider calling Path.mkdir().")

        logger.info(f"Using cache directory at {self._cache_path.resolve()}")

    @cache_path.deleter
    def cache_path(self):
        if self.cache_path and self._cache_path.exists():
            logger.info(f"Deleting cache directory at {self._cache_path.resolve()}")
            self._cache_path.rmdir()
            self._cache_path = None



def get_wide_scale_catalogs() -> list[astrometry.Series]:
    """
    Wide scale catalogs for astrometry.net
    """

    pass
    # indexer = astrometry.series_4100.index_files(
    #     scales=set(range(7,20)),
    #     cache_directory=self._cache_path,
    # )
    # return Series(
    #     [
    #         "index-4200-1024.fits",
    #         "index-4200-2048.fits",
    #         "index-4200-4096.fits",
    #         "index-4200-8192.fits",
    #     ]
    # )
