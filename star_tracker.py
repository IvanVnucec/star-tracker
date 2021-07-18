import catalog
import numpy as np
import transformations as tr 
import plotting as pl


def stars_inside_FOV(points, camera, FOV):
    points_inside = []
    for point in points:
        # camera
        x, y, z = tr.spher_to_cart((camera[0], camera[1], 1.0))
        v1 = np.array([x, y, z])

        # point
        x, y, z = tr.spher_to_cart((point[0], point[1], 1.0))
        v2 = np.array([x, y, z])

        uv1 = v1 / np.linalg.norm(v1)
        uv2 = v2 / np.linalg.norm(v2)
        dot_product = np.dot(uv1, uv2)
        angle = np.arccos(dot_product)
        if angle < np.deg2rad(FOV/2):
            points_inside.append(point)

    return np.vstack(points_inside)


stars = catalog.get_stars(num_of=100_000)

# plot points on the sphere
#pl.plot_on_sphere(stars)

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

stars_fov = stars_inside_FOV(stars, camera, FOV)
pl.plot_on_sphere(stars_fov)

pl.plot_on_canvas(q, stars_fov)

# TODO: stars_2d
