"""
Star representation methods

Links:
    https://astronomy.swin.edu.au/cosmos/E/Epoch
    http://www.siranah.de/html/sail040x.htm
"""


from math import sin, cos


class Star:
    def __init__(self, ra, dec) -> None:
        # TODO: Add comments to function
        self.ra = ra    # rad
        self.dec = dec  # rad

    def get_ra_dec(self):
        """Return right ascention and declination in J2000

        Returns:
            tuple: (right ascention, declination)
        """
        return (self.ra, self.dec)

    def get_xyz(self):
        # TODO: Add description
        ra, dec = self.get_ra_dec()
        r = 1.0 # unity sphere

        x = r * cos(dec) * cos(ra)
        y = r * cos(dec) * sin(ra)
        z = r * sin(dec)

        return (x, y, z)
    