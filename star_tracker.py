import catalog
import plotting as pl
from camera import Camera

camera = Camera()

stars = catalog.get_stars()
pl.plot_on_sphere(stars)

camera_orientation = (0.0, 3.14/2)
stars_2d = camera.capture(stars, camera_orientation)
pl.plot_on_canvas(stars_2d)
