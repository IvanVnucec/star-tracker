"""
About:
    The functions in this file are used to interface with the Tycho-2 star catalog.
"""

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
    """Returns the number of stars from the star catalog. Read all by default."""
    lines = _read_catalog(num_of)

    # extract the star positions from the catalog
    stars_list = [(float(line[153:164]), float(line[167:177]))
                  for line in lines]
    stars = np.array(stars_list)

    return stars
