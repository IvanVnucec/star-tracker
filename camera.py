"""Camera (CCD chip) model."""


import numpy as np
import transformations as tr


class Camera:
    def __init__(self, FOV, f, rhou, rhov, u0, v0) -> None:
        """Camera initialization

        Args:
            FOV (float): Field Of View in degrees.
            f (float): camera focus length in meters
            rhou (float): horizontal pixel size in meters
            rhov (float): vertical pixel size in meters
            u0 (float): horizontal origin of the image plane in meters
            v0 (float): vertical origin of the image plane in meters
        """
        self.FOV = FOV
        self.f = f
        self.rhou = rhou
        self.rhov = rhov
        self.u0 = u0
        self.v0 = v0

        # camera coordiantes in intertial frame
        self.tc = np.array([0.0, 0.0, 0.0])

        # intrinsic camera parameters
        Maff = np.array([
            [1/rhou, 0,    u0],
            [0,   -1/rhov, v0],
            [0,      0,     1]])

        Mproj = np.array([
            [f, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, 1, 0]])

        self.Mint = Maff.dot(Mproj)

    def _get_stars_in_FOV(self, stars, phi, theta):
        """Return only the stars that the star tracker could see.

        Args:
            stars (list): list of stars
            phi (float): orientation angle
            theta (float): orientation angle2

        Returns:
            list: list of stars within FOV
        """
        # TODO: Maybe we could already use camera orientation angles
        # and not convert it to xyz cartesian vector
        stars_fov = []
        for star in stars:
            # camera
            x, y, z = tr.spher_to_cart((phi, theta, 1.0))
            v1 = np.array([x, y, z])

            # star
            x, y, z = tr.spher_to_cart((star[0], star[1], 1.0))
            v2 = np.array([x, y, z])

            # calculate angles between star and camera vectors
            uv1 = v1 / np.linalg.norm(v1)
            uv2 = v2 / np.linalg.norm(v2)
            dot_product = np.dot(uv1, uv2)
            angle = np.arccos(dot_product)

            if angle < np.deg2rad(self.FOV/2):
                stars_fov.append(star)

        return stars_fov

    def _project_on_canvas(self, stars_in_fov, phi, theta):
        """Project stars on unity sphere to 2D camera canvas.

        Args:
            stars_in_fov (list): List of stars inside FOV
            phi (float): orientation angle
            theta (float): orientation angle2

        Returns:
            numpy array: 2D projected stars.
        """
        e = np.array([
            [np.cos(phi) * np.cos(theta)],
            [np.cos(phi) * np.sin(theta)],
            [np.sin(phi)]])
        q = np.vstack((e, 1.0))

        Rc = tr.q_to_R(q)  # quaternion to rot. matrix

        Mext11 = Rc.T
        Mext12 = - Rc.T.dot(self.tc).reshape(3, 1)
        Mext21 = np.zeros((1, 3))
        Mext22 = 1.0
        Mext = np.block([
            [Mext11, Mext12],
            [Mext21, Mext22]])

        M = self.Mint.dot(Mext)

        # TODO: in the end should be [u, v, 1.0] but we are not getting number 1.0
        stars_2d = np.empty((len(stars_in_fov), 3))
        for i, star in enumerate(stars_in_fov):
            star_spher_coord = (star[0], star[1], 1.0)
            U, V, W = tr.spher_to_cart(star_spher_coord)
            point = np.array([U, V, W, 1])
            proj = M.dot(point)
            stars_2d[i] = proj

        return stars_2d

    def capture(self, stars, orientation):
        """Returns captured image of the stars. Needs all
        stars on the sky and camera orientation.

        Args:
            stars (numpy array): all stars that can camera capture
            orientation (tuple): tuple of phi and theta angles
        """
        phi, theta = orientation[0], orientation[1]
        stars_in_fov = self._get_stars_in_FOV(stars, phi, theta)
        stars_2d = self._project_on_canvas(stars_in_fov, phi, theta)

        return stars_2d
