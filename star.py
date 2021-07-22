"""
Star representation methods

Links:
    https://astronomy.swin.edu.au/cosmos/E/Epoch
    http://www.siranah.de/html/sail040x.htm
"""


import transformations as tr


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
        return tr.ra_dec_to_xyz(ra, dec)
    