"""
testbed for pointing vectors to latlon
"""

from ephem import *
from math import degrees as rad2deg
from sys import * 

import math
import datetime
import numpy

# ----------- #

global ANG_TOL, OBF

# ----------- #


ra_in  = float(input("enter CoF Right Ascension (in degrees) => "))  # r.a. for center of solved field [deg]
dec_in = float(input("enter CoF Declination (in degrees) => "))      # dec. for center of solved field [deg]

angtol = 1.0       # [deg] tolerance for ra/dec conditional checks
obf    = 23.439281 # [deg] obliquity of ecliptic 

time_in = now() # TODO exact time of image capture ***REPLACE WITH ACTUAL IMAGE TIMESTAMP UPON CAMERA MODULE INTEGRATION***

target = FixedBody()      # Initialize CoF as a fixed body object
                        
target._ra    = ra_in     # -> initial right ascension 
target._dec   = dec_in    # -> initial declination
target._epoch = time_in   # -> initial epoch snapshot

print( "\nCenter of Field Right ascension is %.3f degree(s), " % trgt._ra )
print(   "Center of Field Declination is %.3f degree(s)" % trgt._dec )
print( "{orientation determined at %s}" % str(time_in) )

zenith = 0 # [deg] angle of camera off zenithal vector

obs = Observer()
