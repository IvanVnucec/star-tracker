"""
Various coordinate transformations.
"""

import numpy as np


def ra_dec_to_xyz(ra, dec):
    """ Unit Spherical to Cartesian coordinates transform. """
    r = 1.0
    x = r * np.cos(dec) * np.cos(ra)
    y = r * np.cos(dec) * np.sin(ra)
    z = r * np.sin(dec)

    return (x, y, z)


def q_to_R(q):
    """Return a Rotation matrix from quaternion. 
    The equations below are for quaternion which 
    is defined as q = [1.0 [e]] but we have 
    q = [[e] 1] where e is 3x1 vector."""
    q0 = q[3]
    q1 = q[0]
    q2 = q[1]
    q3 = q[2]

    R11 = 2 * (q0**2 + q1**2) - 1
    R12 = 2 * (q1*q2 - q0*q3)
    R13 = 2 * (q1*q3 + q0*q2)
    R21 = 2 * (q1*q2 + q0*q3)
    R22 = 2 * (q0**2 + q2**2) - 1
    R23 = 2 * (q2*q3 - q0*q1)
    R31 = 2 * (q1*q3 - q0*q2)
    R32 = 2 * (q2*q3 + q0*q1)
    R33 = 2 * (q0**2 + q3**2) - 1

    return np.block([
        [R11, R12, R13],
        [R21, R22, R23],
        [R31, R32, R33]
    ])
