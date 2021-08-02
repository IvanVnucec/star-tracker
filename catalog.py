"""
About:
    The functions in this file are used to interface with the Tycho-2 star catalog.
"""

from star import Star
import numpy as np

NUM_OF_STARS = 10000
CATALOG = 'data/catalog.dat'


def _read_catalog():
    """Reads lines from catalog file."""
    with open(CATALOG) as f:
        lines = f.readlines()
    
    return lines


def get_stars():
    """Returns stars from the Catalog

    Args:
        num_of (integer, optional): Number of stars to load from the catalog. Defaults to ALL.

    Returns:
        list: List of Star objects. 
    """
    lines = _read_catalog()

    stars = []
    for i in range(0, len(lines), len(lines)//NUM_OF_STARS):
        right_asc_str = lines[i][152:164]    # deg
        declination_str = lines[i][165:177]  # deg
        
        right_asc = np.deg2rad(float(right_asc_str))        # rad
        declination = np.deg2rad(float(declination_str))    # rad
        stars.append(Star(right_asc, declination))

    return stars
