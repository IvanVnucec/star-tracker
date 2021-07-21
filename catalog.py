"""
About:
    The functions in this file are used to interface with the Tycho-2 star catalog.
"""

from star import Star
import numpy as np

ALL = 0
CATALOG = 'data/catalog.dat'


def _read_catalog(num_of=ALL):
    """Reads lines from catalog file."""
    with open(CATALOG) as f:
        if num_of == ALL:
            lines = f.readlines()
        else:
            # TODO: pick random lines
            lines = [f.readline() for _ in range(num_of)]
    
    return lines


def get_stars(num_of=ALL):
    """Returns stars from the Catalog

    Args:
        num_of (integer, optional): Number of stars to load from the catalog. Defaults to ALL.

    Returns:
        list: List of Star objects. 
    """
    lines = _read_catalog(num_of)

    stars = []
    for line in lines:
        right_asc = float(line[153:164])    # deg
        declination = float(line[167:177])  # deg
        stars.append(Star(right_asc, declination))

    return stars
