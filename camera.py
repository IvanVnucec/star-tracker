"""Camera (CCD chip) model."""


import numpy as np
import transformations as tr
import plotting as pl


class Camera:
    def __init__(self):
        """Camera initialization

        Args:
            FOV (float): Field Of View in degrees.
            f (float): camera focus length in meters
            rhou (float): horizontal pixel size in meters
            rhov (float): vertical pixel size in meters
            u0 (float): horizontal origin of the image plane in meters
            v0 (float): vertical origin of the image plane in meters
        """
        # camera parameters
        FOV = 90        # deg
        f = 1e-3                # m
        px = py = 1e-2          # m
        mx = my = 1e6           # pixels/m
        s = 0.0                 # skew
        C = np.zeros((3, 1))    # m
        
        self.FOV = FOV
        self.f = f
        self.px = px
        self.py = py
        self.mx = mx
        self.my = my
        self.s  = s
        self.C  = C

        ax = f * mx     # pixels
        ay = f * my     # pixels
        x0 = mx * px    # pixels
        y0 = my * py    # pixels

        self.K = np.array([
            [ax, s, x0],
            [0, ay, y0],
            [0, 0,   1]
        ])

    def _get_stars_in_FOV(self, stars, orientation):
        """Return only the stars that the star tracker could see.

        Args:
            stars (list): list of stars
            orientation (tuple): camera orientation

        Returns:
            list: list of stars within FOV
        """
        # TODO: Maybe we could already use camera orientation angles
        # and not convert it to xyz cartesian vector
        
        # camera
        x, y, z = tr.ra_dec_to_xyz(orientation[0], orientation[1])
        v1 = np.array([x, y, z])

        stars_fov = []
        for star in stars:
            # star
            x, y, z = star.get_xyz()
            v2 = np.array([x, y, z])

            # calculate angles between star and camera vectors
            uv1 = v1 / np.linalg.norm(v1)
            uv2 = v2 / np.linalg.norm(v2)
            dot_product = np.dot(uv1, uv2)
            angle = np.arccos(dot_product)

            if angle < np.deg2rad(self.FOV/2):
                stars_fov.append(star)

        return stars_fov

    def _project_on_canvas(self, stars_in_fov, orientation):
        """Project stars on unity sphere to 2D camera canvas.

        Args:
            stars_in_fov (list): List of stars inside FOV
            orientation (tuple): camera orientation

        Returns:
            numpy array: 2D projected stars.
        """
        phi, theta = orientation[0], orientation[1]
        e = np.array([
            [np.cos(phi) * np.cos(theta)],
            [np.cos(phi) * np.sin(theta)],
            [np.sin(phi)]])
        q = np.vstack((e, 1.0))
        q = q / np.linalg.norm(q)

        R = tr.q_to_R(q)  # quaternion to rot. matrix
        print(R)
        t = -R.dot(self.C)
        P = self.K.dot(np.block([R, t]))

        stars_2d = np.empty((len(stars_in_fov), 3))
        for i, star in enumerate(stars_in_fov):
            U, V, W = star.get_xyz()
            point = np.array([U, V, W, 1])
            proj = P.dot(point)
            stars_2d[i] = proj

        return stars_2d

    def capture(self, stars, orientation):
        """Returns captured image of the stars. Needs all
        stars on the sky and camera orientation.

        Args:
            stars (numpy array): all stars that can camera capture
            orientation (tuple): tuple of phi and theta angles
        """
        stars_in_fov = self._get_stars_in_FOV(stars, orientation)
        pl.plot_on_sphere(stars_in_fov)
        stars_2d = self._project_on_canvas(stars_in_fov, orientation)

        return stars_2d
