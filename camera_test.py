'''
testing out camera
'''

from Camera import *

c = Camera(-45.1,33.2,5000,12,45,60)

c.print_position()
c.print_attitude_eq()
c.print_attitude_q()
c.print_attitude_dcm()