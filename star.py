"""
Star representation methods

Links:
    https://astronomy.swin.edu.au/cosmos/E/Epoch
    http://www.siranah.de/html/sail040x.htm
"""


class Star:
    def __init__(self, ra, dec) -> None:
        # TODO: Add comments to function
        self.ra = ra
        self.dec = dec

    def get_coords(self):
        """Return right ascention and declination in J2000

        Returns:
            tuple: (right ascention, declination)
        """
        return (self.ra, self.dec)

    