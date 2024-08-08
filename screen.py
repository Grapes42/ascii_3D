from os import system, name
from copy import copy
import numpy as np

X = 1
Y = 0

class Screen():
    def __init__(self, height, width, origin_y=0, origin_x=0) -> None:
        self.height = height
        self.width = width
        self.array = np.full((height, width), " ")

        self.origin_y = origin_y
        self.origin_x = origin_x

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux
        else:
            _ = system('clear')

    def print(self, clear=True):
        screen_str = ""

        for y in range(len(self.array)):
            line = ""
            for x in range(len(self.array[0])):
                line += str(self.array[y, x])
            screen_str += f"{line}\n"

        print(screen_str)

        if clear:
            self.clear()

    def plot(self, y, x, char="#"):
        y = round(y) + self.origin_y
        x = round(x) + self.origin_x

        if (y < 0) or (y > self.height-1):
            in_y_boundary = False
        else:
            in_y_boundary = True

        if (x < 0) or (x > self.width-1):
            in_x_boundary = False
        else:
            in_x_boundary = True

        if in_y_boundary and in_x_boundary:
            self.array[y, x] = char

    def line(self, coord0, coord1, step_size=1):
        rise = coord0[X] - coord1[X]
        run = coord0[Y] - coord1[Y]

        if rise != 0:
            gradient = run/rise

            if coord0[X] <= coord1[X]:
                pos_y, pos_x = copy(coord0[Y]), copy(coord0[X])
                end_y, end_x = copy(coord1[Y]), copy(coord1[X])
            else:
                pos_y, pos_x = copy(coord1[Y]), copy(coord1[X])
                end_y, end_x = copy(coord0[Y]), copy(coord0[X])

            while pos_x <= end_x:
                self.plot(y=pos_y, x=pos_x)
                
                pos_x += step_size
                pos_y += gradient * step_size

        else:
            if coord0[Y] <= coord1[Y]:
                pos_y, pos_x = copy(coord0[Y]), copy(coord0[X])
                end_y, end_x = copy(coord1[Y]), copy(coord1[X])
            else:
                pos_y, pos_x = copy(coord1[Y]), copy(coord1[X])
                end_y, end_x = copy(coord0[Y]), copy(coord0[X])

            while pos_y <= end_y:
                self.plot(y=pos_y, x=pos_x)
                pos_y += step_size

    def construct_pairs(self, points, pairs, step_size=1):  
        for pair in pairs:
            self.line(points[pair[0], 0], points[pair[1], 0])
