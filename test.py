import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

from catalog import get_stars


def get_colors(n):
    np.random.seed(1337)
    return np.random.rand(n, 3)


def plot_2d_points(X, Y, x0, y0):
    rect = patch.Rectangle((0, 0), 2*x0, 2*y0, linewidth=3, edgecolor='r', facecolor='none')
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(X, Y, c=get_colors(len(X)))
    ax.set_box_aspect(aspect=1)
    ax.set_xlim(0, 2*x0)
    ax.set_ylim(0, 2*y0)
    ax.grid(True)
    ax.add_patch(rect)


def plot_3d_points(X, Y, Z):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.scatter(X, Y, Z, c=get_colors(len(X)))
    ax.set_zlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_xlim3d(-1, 1)


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

XYZ = []
RADEC = get_stars()
for radec in RADEC:
    XYZ.append(radec.get_xyz())

XYZ = np.array(XYZ)

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
plot_2d_points(Px, Py, x0, y0)

plt.show()
