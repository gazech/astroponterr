"""
Class for star camera
"""

import numpy as np 
from Quaternion import Quat 

class Camera(object):

    def __init__(self, \
                    lat  = None, \
                    lon  = None, \
                    alt  = None, \
                    ra   = None, \
                    dec  = None, \
                    roll = None, \
                    fov  = None, \
                    res  = None  \
                ):

        self.position = np.array([lat,lon,alt]) 
        self.attitude = Quat(equatorial=[ra,dec,roll])

    def print_position(self):
        """
        Print out camera position info
        """
        print("Camera Position:")
        print("\tLattitude      %+3.1f [degrees]" % self.position[0])
        print("\tLongitude      %+3.1f [degrees]" % self.position[1])
        print("\tAltitude (HAE) %+6.2f [meters]"  % self.position[2])
        print()

    def print_attitude_eq(self):
        """
        Print out camera attitude info in equatorial coords
        """

        attitude = self.attitude._get_equatorial()

        print("Camera Attitude:")
        print("\tRight Asc.  %+3.1f [degrees]" % attitude[0])
        print("\tDeclination %+3.1f [degrees]" % attitude[1])
        print("\tRoll        %+3.1f [degrees]" % attitude[2])
        print()

    def print_attitude_q(self):
        """
        Print out camera attitude info in quaternion coords
        """

        attitude = self.attitude._get_q()

        print("Camera Attitude:")
        print("\tX  %+6.4f" % attitude[0])
        print("\tY  %+6.4f" % attitude[1])
        print("\tZ  %+6.4f" % attitude[2])
        print("\tW  %+6.4f" % attitude[3])
        print()

    def print_attitude_dcm(self):
        """
        Print out camera attitude info in quaternion coords
        """

        attitude = self.attitude._get_transform()

        print("Camera Attitude:")
        print("\t[%+.5f %+.5f %+.5f]" % (attitude[0][0],attitude[1][0],attitude[2][0]))
        print("\t[%+.5f %+.5f %+.5f]" % (attitude[0][1],attitude[1][1],attitude[2][1]))
        print("\t[%+.5f %+.5f %+.5f]" % (attitude[0][2],attitude[1][2],attitude[2][2]))
        print()

    def __eq__(self, other):
        """
        Determine if camera states are equivalent
        """
        return 0

    # def __repr__(self):
    # return "Point({0.x!r}, {0.y!r})".format(self)
    # def __str__(self):
    # return "({0.x!r}, {0.y!r})".format(self)