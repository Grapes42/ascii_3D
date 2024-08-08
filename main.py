import numpy as np
import cv2

import time

from screen import Screen
from projection import Projection
from data_types import *

screen_height = 150
screen_width = 500

screen = Screen(height=screen_height, width=screen_width)
projection = Projection(screen_height=screen_height, screen_width=screen_width, scale=1, 
                        fx=800, fy=800)


points, pairs = projection.cube_by_center(origin=Coord_3D(0, 0, 10),
                                    width=2,
                                    height=1,
                                    depth=2)
screen.construct_pairs(pairs=pairs, points=points)



screen.print()

time.sleep(.1)
