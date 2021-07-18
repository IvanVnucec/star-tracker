"""
Various coordinate transformations.
"""

import numpy as np


def spher_to_cart(p):
    """ Spherical to Cartesian coordinates transform. """
    phi, theta, r = p[0], p[1], p[2]

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    return x, y, z
