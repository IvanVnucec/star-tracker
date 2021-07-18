"""
Functions used to plot the stars.
"""


import numpy as np
import matplotlib.pyplot as plt
import transformations as tr


def plot_on_sphere(points):
    # create a sphere
    r = 1.0
    phi, theta = np.mgrid[0.0:np.pi:100j, 0.0:2.0*np.pi:100j]
    x, y, z = tr.spher_to_cart((phi, theta, r))

    # import data
    r = 1.0
    phi, theta = np.hsplit(points, 2)
    xx, yy, zz = tr.spher_to_cart((phi, theta, r))

    # set colours and render
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1,
                    color='c', alpha=0.1, linewidth=0)
    ax.scatter(xx, yy, zz, color="k", s=1)
    ax.set_box_aspect(aspect=(1, 1, 1))
    plt.show()


def plot_on_canvas(q, stars_fov):
    # project points on the sphere to 2D frame
    f = 0.1 # meters
    rhou = 0.0001 # pixel sizes in meters
    rhov = 0.0001
    u0 = 0.01 # pixel locations of the origin of the image plane in meters
    v0 = 0.01

    Maff = np.array([
        [1/rhou, 0,    u0],
        [0,   -1/rhov, v0],
        [0,      0,     1]])
    print('Maff\n', Maff)

    Mproj = np.array([
        [f, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, 1, 0]])
    print('Mproj\n', Mproj)

    tc = np.array([0.0, 0.0, 0.0]) # camera coordiantes in intertial frame
    Rc = tr.q_to_R(q) # quaternion to rot. matrix

    Mext11 = Rc.T
    Mext12 = - Rc.T.dot(tc).reshape(3, 1)
    Mext21 = np.zeros((1, 3))
    Mext22 = 1.0
    Mext = np.block([
        [Mext11, Mext12],
        [Mext21, Mext22]])
    print('Mext\n', Mext)

    M = Maff.dot(Mproj).dot(Mext)
    print('M\n', M)

    stars_2d = np.empty((len(stars_fov), 3)) # in the end should be [u, v, 1]
    for i, star in enumerate(stars_fov):
        star_spher_coord = (star[0], star[1], 1.0) 
        U, V, W = tr.spher_to_cart(star_spher_coord)
        point = np.array([U, V, W, 1])
        proj = M.dot(point)
        stars_2d[i] = proj

    print('stars_2d\n', stars_2d)

    # plot 2D points
    u = stars_2d[:,0]
    v = stars_2d[:,1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(u, v, s=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
