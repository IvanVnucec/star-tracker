import matplotlib.pyplot as plt
import numpy as np

def plot_on_sphere(points):
    # create a sphere
    r = 1.0
    phi, theta = np.mgrid[0.0:np.pi:100j, 0.0:2.0*np.pi:100j]
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    # import data
    phi, theta = np.hsplit(points, 2)
    xx = np.sin(phi) * np.cos(theta)
    yy = np.sin(phi) * np.sin(theta)
    zz = np.cos(phi)

    # set colours and render
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color='c', alpha=0.1, linewidth=0)
    ax.scatter(xx, yy, zz, color="k", s=1)
    ax.set_box_aspect(aspect = (1,1,1))
    plt.show()    


# read from the star catalog
with open('data/catalog.dat') as f:
    #lines = f.readlines()
    lines = [f.readline() for _ in range(1000)]

# extract the star positions from the catalog
stars_list = [(float(line[153:164]), float(line[167:177])) for line in lines]
stars = np.array(stars_list)

# plot points on the sphere
#plot_on_sphere(stars)

# camera
FOV = 20.0 / 180.0 * np.pi

# camera orientation
phi, theta = 0.0, 0.0
e = np.array([
    [np.cos(phi) * np.cos(theta)],
    [np.cos(phi) * np.sin(theta)],
    [np.sin(phi)]])
q = np.vstack((e, 1.0))

# TODO: plot points on the sphere within FOV
# calculate camera vector
# calculate star vectors
# for every star vector
    # calculate angle between star and camera vector
    # if angle < FOV / 2
        # plot
    # else
        # don't plot
