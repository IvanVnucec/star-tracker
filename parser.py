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
    phi, theta = np.hsplit(pos_arr, 2)
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
pos_list = [(float(line[153:164]), float(line[167:177])) for line in lines]
pos_arr = np.array(pos_list)

plot_on_sphere(pos_arr)

