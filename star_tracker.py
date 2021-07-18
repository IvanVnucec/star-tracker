import catalog
import plotting as pl
from camera import Camera


NUM_OF_STARS = 10_000

# camera parameters
FOV = 20        # deg
f = 0.1         # m
rhou = 0.0001   # m
rhov = 0.0001   # m
u0 = 0.01      # m
v0 = 0.01       # m
camera = Camera(FOV, f, rhou, rhov, u0, v0)

stars = catalog.get_stars(NUM_OF_STARS)
# pl.plot_on_sphere(stars)

# TODO: pick some randomly generated orientation
camera_orientation = (3.14159/6, -1.0)

stars_2d = camera.capture(stars, camera_orientation)
pl.plot_on_canvas(stars_2d)
