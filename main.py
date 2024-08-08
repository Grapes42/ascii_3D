import numpy as np
import cv2

from screen import Screen
from projection import Projection
from data_types import *

screen_height = 150
screen_width = 300

screen = Screen(height=screen_height, width=screen_width)
projection = Projection(screen_height=screen_height, screen_width=screen_width)

points, pairs = projection.cube_by_center(origin=Coord_3D(0, 0, 0),
                                          width=.2,
                                          height=.1,
                                          depth=1)
screen.construct_pairs(pairs=pairs, points=points)

points, pairs = projection.cube_by_center(origin=Coord_3D(.2, 0, 0),
                                          width=.2,
                                          height=.1,
                                          depth=1)
screen.construct_pairs(pairs=pairs, points=points)

points, pairs = projection.cube_by_center(origin=Coord_3D(0, 0.4, 0),
                                          width=.2,
                                          height=.1,
                                          depth=1)
screen.construct_pairs(pairs=pairs, points=points)

points, pairs = projection.cube_by_center(origin=Coord_3D(.2, 0.4, 0),
                                          width=.2,
                                          height=.1,
                                          depth=1)
screen.construct_pairs(pairs=pairs, points=points)

screen.print()