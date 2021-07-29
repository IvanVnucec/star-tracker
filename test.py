import numpy as np
import matplotlib.pyplot as plt


def get_colors(n):
    np.random.seed(1337)
    return np.random.rand(n, 3)


def plot_2d_points(X, Y, x0=0.0, y0=0.0):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(X, Y, c=get_colors(len(X)))
    #ax.set_xlim([-100, 1100])
    #ax.set_ylim([-100, 2100])
    ax.set_box_aspect(aspect=1)
    ax.grid(True)


def plot_3d_points(X, Y, Z):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    #ax.set_aspect('equal')
    ax.scatter(X, Y, Z, c=get_colors(len(X)))


def gen_points(z=1.0, n=5):
    cx = cy = 0.0
    r = 1.0
    
    theta = np.linspace(0, 2*np.pi, num=n)
    x = r * np.cos(theta) + cx
    y = r * np.sin(theta) + cy
    z = z * np.ones_like(x)

    # n*3
    return np.block([[x], [y], [z]]).T


def to_hom(p):
    return np.append(p, 1.0)


def from_hom(ph):
    return ph[0:2] / ph[-1]



f = 1e-3                # m
px = py = 1e-2          # m
mx = my = 1e6           # pixels/m
s = 0.0                 # skew
C = np.zeros((3, 1))    # m
R = np.eye(3)

t = -R.dot(C)

ax = f * mx     # pixels
ay = f * my     # pixels
x0 = mx * px    # pixels
y0 = my * py    # pixels

K = np.array([
    [ax, s, x0],
    [0, ay, y0],
    [0, 0,   1]
])

P = K.dot(np.block([R, t]))

XYZ = gen_points(z=1.0, n=20) # m
XYZ = np.vstack((XYZ, gen_points(z=2.0, n=6))) # m

XYZ1 = np.empty((XYZ.shape[0], 4))
for i, xyz in enumerate(XYZ):
    XYZ1[i] = to_hom(xyz)

x = np.empty((XYZ1.shape[0], 3))
for i, X in enumerate(XYZ1):
    x[i] = P.dot(X.T)

PxPy = np.empty(((XYZ1.shape[0], 2)))
for i, x_hom in enumerate(x):
    PxPy[i] = from_hom(x_hom)

X, Y, Z = XYZ.T
plot_3d_points(X, Y, Z)

Px, Py = PxPy.T
plot_2d_points(Px, Py)

plt.show()
