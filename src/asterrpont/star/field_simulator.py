"""utilities for simulating star fields"""

from pathlib import Path

import polars as pl

# see: https://rhodesmill.org/skyfield/example-plots.html#neowise-chart


class StarField:
    """
    Class for simulating star fields.
    """

    def __init__(self, catalog: pl.DataFrame):
        self._catalog = catalog

    @property
    def catalog(self):
        """
        Return the catalog.
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog: pl.DataFrame):
        raise ValueError("Catalog is read-only.")

    def generate_scene(
        self,
        right_ascension: float,
        declination: float,
        field_of_view: tuple[float, float],
        magnitude_limit: float = 10.0,
    ):
        """
        Generate a star field for the given scene parameters
        """
        pass


def main(catalog_path: Path = Path.home / "workspace" / "data" / "athyg" / "athyg.csv"):
    """
    Main function for testing the StarField class.
    """
    catalog = pl.read_csv(catalog_path)
    star_fielder = StarField(catalog)

    # get_constellation

    return star_fielder


if __name__ == "__main__":
    main()
