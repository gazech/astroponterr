# Huntington Gazecki
# Star Tracker Project - Summer 2018
# Started June 6th, 2018
#
# Master Script

from ephem import *
from math import degrees as rad2deg
from sys import exit 

import math
import datetime
import numpy

# ----------- #

global angtol, obf

# ----------- #


ra_in  = float(input("enter CoF Right Ascension (in degrees) => "))  # r.a. for center of solved field [deg]
dec_in = float(input("enter CoF Declination (in degrees) => "))      # dec. for center of solved field [deg]

angtol = 1.0       # [deg] tolerance for ra/dec conditional checks
obf    = 23.439281 # [deg] obliquity of ecliptic 

if abs(ra_in)  <= angtol : # ra check
    print("\nWARNING: Indicated right ascension value is close to zero, be sure entry is in degrees.")
    racheck = input("Continue?\nYes (1) or No (0): ")
    
    if int(racheck) == 1:
        print("Right ascension entry validated. Continuing...")
    elif int(racheck) == 0:
        print("Exiting...")
        exit()
    else:
        print("Invalid entry. Exiting...")
        exit()    
   
if abs(dec_in) <= angtol : # dec check
    print("\nWARNING: Indicated declination value is close to zero, be sure entry is in degrees.")
    deccheck = input("Continue?\nYes (1) or No (0): ")
    
    if int(deccheck) == 1:
        print("Declination entry validated. Continuing...")
    elif int(deccheck) == 0:
        print("Exiting...")
        exit()
    else:
        print("Invalid entry. Exiting...") 
        exit()


time_in = now() # exact time of image capture ***REPLACE WITH ACTUAL IMAGE TIMESTAMP UPON CAMERA MODULE INTEGRATION***

trgt = FixedBody()      # Initialize CoF as a fixed body object
                        
trgt._ra    = ra_in     # -> initial right ascension 
trgt._dec   = dec_in    # -> initial declination
trgt._epoch = time_in   # -> initial epoch snapshot

print( "\nRight ascension is %.3f degree(s), " % trgt._ra )
print( "Declination is %.3f degree(s)" % trgt._dec )
print( "{orientation determined at %s}" % str(time_in) )

