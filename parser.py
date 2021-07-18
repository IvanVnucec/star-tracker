import matplotlib.pyplot as plt
import numpy as np


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


def stars_inside_FOV(points, camera, FOV):
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

    return np.vstack(points_inside)


def q_to_R(q):
    # q = [[e] 1]
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


# read from the star catalog
with open('data/catalog.dat') as f:
    #lines = f.readlines()
    lines = [f.readline() for _ in range(100)]

# extract the star positions from the catalog
stars_list = [(float(line[153:164]), float(line[167:177])) for line in lines]
stars = np.array(stars_list)

# plot points on the sphere
#plot_on_sphere(stars)

# camera
FOV = 20.0 # degrees

# camera orientation
# TODO: pick some random orientation
camera = np.array([np.pi/6, -1.0])

r = 1.0
phi, theta = camera[0], camera[1]
e = np.array([
    [np.cos(phi) * np.cos(theta)],
    [np.cos(phi) * np.sin(theta)],
    [np.sin(phi)]])
q = np.vstack((e, 1.0))

# plot points on the sphere within FOV
stars_fov = stars_inside_FOV(stars, camera, FOV)
plot_on_sphere(stars_fov)

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
Rc = q_to_R(q) # quaternion to rot. matrix

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
    U, V, W = spher_to_cart(star_spher_coord)
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
ax.set_box_aspect(aspect = 1)
plt.show()

# TODO: stars_2d
