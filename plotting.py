"""
Functions used to plot the stars.
"""


import numpy as np
import matplotlib.pyplot as plt
import transformations as tr


def plot_on_sphere(stars):
    # create a sphere
    phi, theta = np.mgrid[0.0:np.pi:100j, 0.0:2.0*np.pi:100j]
    x, y, z = tr.ra_dec_to_xyz(phi, theta)

    # import data
    xx   = np.empty(len(stars)) 
    yy = np.empty(len(stars))
    zz = np.empty(len(stars))
    for i, star in enumerate(stars):
        xx[i], yy[i], zz[i] = star.get_xyz()

    # set colours and render
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color='c', alpha=0.1, linewidth=0)
    ax.scatter(xx, yy, zz, color="k", s=1)
    ax.set_box_aspect(aspect=(1, 1, 1))
    plt.show()


def plot_on_canvas(stars):
    """Plot stars on 2D canvas with equal axis scaling.

    Args:
        stars (numpy array): 2D star representations.
    """
    u = stars[:, 0]
    v = stars[:, 1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(u, v, s=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
