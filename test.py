import numpy as np
import matplotlib.pyplot as plt


def plot_2d_points(X, Y):
    fig = plt.figure()
    ax = fig.add_subplot()
    #ax.set_aspect('equal')
    ax.scatter(X, Y)
    plt.show()


def plot_3d_points(X, Y, Z):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    #ax.set_aspect('equal')
    ax.scatter(X, Y, Z)
    plt.show()


def generate_points(n=1000):
    x = np.array([0, 1, 1]).reshape((3, 1))
    y = np.array([0, 1, 2]).reshape((3, 1))
    z = np.array([1, 1, 1]).reshape((3, 1))

    """
    r = 1.0
    theta = np.random.uniform(0, 0.02, (n, 1)) # valid range [0, 2pi]
    phi =   np.random.uniform(0, 0.02, (n, 1)) # valid range [0,  pi]
    
    sin = np.sin
    cos = np.cos

    x = r * cos(theta) * sin(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(phi)
    """
    return x, y, z


def get_camera_matrix(f, dx, dy, x0, y0, t, R):
    ax = f/dx
    ay = f/dy

    # Camera calibration matrix
    K = np.array([
        [ax,  0,  x0],
        [ 0, ay,  y0],
        [ 0,  0,   1]
    ])

    # Camera matrix 3x4
    P_ = np.block([R, t.reshape((3, 1))])
    P = K.dot(P_)

    return P


# Internal parameters
f  = 1e-3 # focal length in meters
dx = 1e-6 # pixel dimension in meters
dy = 1e-6 # pixel dimension in meters
x0 = 1e-2 # CCD centre in meters
y0 = 1e-2 # CCD centre in meters

# External parameters
R = np.eye(3)               # World to Camera coords 
t = np.array([0, 0, 0])     # in Camera coords in meters


P = get_camera_matrix(f, dx, dy, x0, y0, t, R)

X, Y, Z = generate_points()

#plot_3d_points(X, Y, Z)

XYZ1 = np.hstack((X, Y, Z, np.ones_like(X)))

xy1 = np.empty((XYZ1.shape[0], 3))
# Points in pixel
for i, xyz1 in enumerate(XYZ1):
    xy1_ = P.dot(xyz1)
    xy1[i] = xy1_ / xy1_[-1]

print(xy1)
plot_2d_points(xy1[:,0], xy1[:,1])