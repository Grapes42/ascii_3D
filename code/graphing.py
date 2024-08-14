from copy import copy
import numpy as np

X = 1
Y = 0

class Graphing():
    def __init__(self, height, width, origin_y=0, origin_x=0, y_correction=.5) -> None:
        # Sets the width and height of the character array
        self.height = height
        self.width = width
        self.array = np.full((self.height, self.width), " ")

        # Sets the origin of the graph.
        # Most often this will be 1/2 character array width 
        # by 1/2 the character array height
        self.origin_y = origin_y
        self.origin_x = origin_x

        # As characters are often taller than they are wide
        # a y correction value is needed
        self.y_correction = y_correction

    # Resets the graph
    def clear(self):
        self.array = np.full((self.height, self.width), " ")

    def plot(self, y, x, char="#"):
        # Round points to character array
        y = round(y*self.y_correction + self.origin_y)
        x = round(x + self.origin_x)

        # Check if point is within the screen's Y boundary
        if (y < 0) or (y > self.height-1):
            in_y_boundary = False
        else:
            in_y_boundary = True

        # Check if point is within the screen's X boundary
        if (x < 0) or (x > self.width-1):
            in_x_boundary = False
        else:
            in_x_boundary = True

        # If point is in both boundaries, render it
        if in_y_boundary and in_x_boundary:
            self.array[y, x] = char

    def line(self, coord0, coord1, step_size=1, char="#"):
        rise = coord0[X] - coord1[X]
        run = coord0[Y] - coord1[Y]

        # If the rise is not 0, then do the gradient calculation as normal
        if rise != 0:
            gradient = run/rise

            if coord0[X] <= coord1[X]:
                pos_y, pos_x = copy(coord0[Y]), copy(coord0[X])
                end_y, end_x = copy(coord1[Y]), copy(coord1[X])
            else:
                pos_y, pos_x = copy(coord1[Y]), copy(coord1[X])
                end_y, end_x = copy(coord0[Y]), copy(coord0[X])

            while pos_x <= end_x:
                self.plot(y=pos_y, x=pos_x, char=char)
                
                pos_x += step_size
                pos_y += gradient * step_size

        # If the rise is 0, go straight up without x travel
        else:
            if coord0[Y] <= coord1[Y]:
                pos_y, pos_x = copy(coord0[Y]), copy(coord0[X])
                end_y, end_x = copy(coord1[Y]), copy(coord1[X])
            else:
                pos_y, pos_x = copy(coord1[Y]), copy(coord1[X])
                end_y, end_x = copy(coord0[Y]), copy(coord0[X])

            while pos_y <= end_y:
                self.plot(y=pos_y, x=pos_x, char=char)
                pos_y += step_size

    # Plots lines between all specified points and pairs
    def construct_pairs(self, points, pairs, step_size=1, char="#"):  
        for pair in pairs:
            self.line(points[pair[0], 0], points[pair[1], 0], char=char, step_size=step_size)
