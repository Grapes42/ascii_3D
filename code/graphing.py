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

    def plot(self, y, x, char="#", y_correction=True, add_origin=True):
        if y_correction:
            y *= self.y_correction
        if add_origin:
            y += self.origin_y
            x += self.origin_x

        # Round points to character array
        y = round(y)
        x = round(x)


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

    def get_first(self, axis0, axis1, coord0, coord1):

        if coord0[axis0] <= coord1[axis0]:
            pos_0 = copy(coord0[axis0])
            end_0 = copy(coord1[axis0])

            pos_1 = copy(coord0[axis1])
        
        else:
            pos_0 = copy(coord1[axis0])
            end_0 = copy(coord0[axis0])

            pos_1 = copy(coord1[axis1])

        return pos_0, end_0, pos_1

    def line(self, coord0, coord1, step_size=1, char="#", rounding=4, y_correction=True, add_origin=True):
        run = coord0[X] - coord1[X]
        rise = coord0[Y] - coord1[Y]

        if run != 0:
            gradient = round(rise/run, rounding)

            if abs(gradient) <= 1:
                pos_x, end_x, pos_y = self.get_first(axis0=X, axis1=Y, 
                                                    coord0=coord0, coord1=coord1)
                
                while pos_x <= end_x:
                    self.plot(y=pos_y, x=pos_x, char=char, y_correction=y_correction, add_origin=add_origin)
                    pos_x += step_size
                    pos_y += step_size * gradient

            elif abs(gradient) > 1:
                pos_y, end_y, pos_x = self.get_first(axis0=Y, axis1=X,
                                                     coord0=coord0, coord1=coord1)
                
                while pos_y <= end_y:
                    self.plot(y=pos_y, x=pos_x, char=char, y_correction=y_correction, add_origin=add_origin)
                    pos_y += step_size
                    pos_x += step_size / gradient
        else:
            pos_y, end_y, pos_x = self.get_first(axis0=Y, axis1=X,
                                                    coord0=coord0, coord1=coord1)
            
            while pos_y <= end_y:
                self.plot(y=pos_y, x=pos_x, char=char, y_correction=y_correction, add_origin=add_origin)
                pos_y += step_size

    # Plots lines between all specified points and pairs
    def construct_pairs(self, points, pairs, step_size=1, char="#"):  
        for pair in pairs:
            self.line(points[pair[0], 0], points[pair[1], 0], char=char, step_size=step_size)

    def rectangle(self, coord0, coord1, char="#", y_correction=True, add_origin=True):
        a = copy(coord0)
        b = copy(coord0)

        c = copy(coord1)
        d = copy(coord1)

        b[X] = c[X]
        d[X] = a[X]

        self.line(a, b, step_size=1, char=char, y_correction=y_correction, add_origin=add_origin)
        self.line(b, c, step_size=1, char=char, y_correction=y_correction, add_origin=add_origin)
        self.line(c, d, step_size=1, char=char, y_correction=y_correction, add_origin=add_origin)
        self.line(d, a, step_size=1, char=char, y_correction=y_correction, add_origin=add_origin)

    def fill(self, char="#"):
        self.array = np.full((self.height, self.width), char)

    def write(self, message, y, x, y_correction=False, add_origin=False, gap_char=None):
        for char in message:
            if char != gap_char:
                self.plot(y=y, x=x, char=char, y_correction=y_correction, add_origin=add_origin)
            x += 1