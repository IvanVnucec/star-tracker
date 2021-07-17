import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.function_base import diff


def spher_to_cart(p):
    phi, theta, r = p[0], p[1], p[2]

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    return x, y, z


def plot_on_sphere(points):
    # create a sphere
    r = 1.0
    phi, theta = np.mgrid[0.0:np.pi:100j, 0.0:2.0*np.pi:100j]
    x, y, z = spher_to_cart((phi, theta, r))

    # import data
    r = 1.0
    phi, theta = np.hsplit(points, 2)
    xx, yy, zz = spher_to_cart((phi, theta, r))

    # set colours and render
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color='c', alpha=0.1, linewidth=0)
    ax.scatter(xx, yy, zz, color="k", s=1)
    ax.set_box_aspect(aspect = (1,1,1))
    plt.show()    


def plot_on_sphere_inside_FOV(points, camera, FOV):
    points_inside = []
    for point in points:
        # camera
        x, y, z = spher_to_cart((camera[0], camera[1], 1.0))
        v1 = np.array([x, y, z])

        # point
        x, y, z = spher_to_cart((point[0], point[1], 1.0))
        v2 = np.array([x, y, z])

        uv1 = v1 / np.linalg.norm(v1)
        uv2 = v2 / np.linalg.norm(v2)
        dot_product = np.dot(uv1, uv2)
        angle = np.arccos(dot_product)
        if angle < np.deg2rad(FOV/2):
            points_inside.append(point)

    plot_on_sphere(np.array(points_inside))


# read from the star catalog
with open('data/catalog.dat') as f:
    #lines = f.readlines()
    lines = [f.readline() for _ in range(10000)]

# extract the star positions from the catalog
stars_list = [(float(line[153:164]), float(line[167:177])) for line in lines]
stars = np.array(stars_list)

# plot points on the sphere
plot_on_sphere(stars)

# camera
FOV = 20.0 # degrees

# camera orientation
# TODO: pick some random orientation
camera = np.array([np.pi/3, -1.0])

r = 1.0
phi, theta = camera[0], camera[1]
e = np.array([
    [np.cos(phi) * np.cos(theta)],
    [np.cos(phi) * np.sin(theta)],
    [np.sin(phi)]])
q = np.vstack((e, 1.0))

# plot points on the sphere within FOV
plot_on_sphere_inside_FOV(stars, camera, FOV)
