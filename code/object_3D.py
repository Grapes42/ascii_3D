"""
File: object_3D.py

Usage: Creates a blueprint for all objects. 
Allows easy changing of an object parameters, and easy rotation and translation.
"""

import math

# Constants
Y = 0
X = 1
Z = 2

A = 0
B = 1

pi = 3.14159265359

class Object3D():
    def __init__(self, array=[], pairs=[], char="#") -> None:
        self.array = array # Array of the object's co-ordinates 
        self.pairs = pairs # Pairs to construct lines between
        self.char = char # Character used to construct shape

    def __str__(self) -> str:
        return f"Array: {self.array}\nPairs: {self.pairs}\nChar: {self.char}"
    
    def move(self, axis, amount) -> None:
        for point in self.array[0]:
            point[axis] += amount

    def rotate(self, origin, rads, axis) -> None:
        axes = [Y, X, Z]

        axes.remove(axis)

        # Define rotation origin
        a_o = origin[axes[0]]
        b_o = origin[axes[1]]

        for point in self.array[0]:
            # Initial points
            a_i = point[axes[0]]
            b_i = point[axes[1]]

            # Distances from origin to initial point
            a_from_origin = abs(a_i - a_o)
            b_from_origin = abs(b_i - b_o)

            # Temporary fix to fix a point with x=0, y=0 bugging out when rotated around y or x
            if a_from_origin == 0 and b_from_origin == 0:
                a_from_origin = 0.0001

            # Uses the Pythagorean theorum to find the radius of the rotation
            radius = math.sqrt( a_from_origin**2 + b_from_origin**2 )



            # Determine what quadrant of the circle the point is in
            # and adjust the offset and trig accordingly

            # Both positive
            if b_i > b_o and a_i > a_o:
                angle_corrector = math.atan(b_from_origin / a_from_origin)

            # b positive, a negative
            elif b_i > b_o and a_i < a_o:
                angle_corrector = math.atan(a_from_origin / b_from_origin) + (.5 * pi)

            # Both negative
            elif b_i < b_o and a_i < a_o:
                angle_corrector = math.atan(b_from_origin / a_from_origin) + (pi)

            # b negative, a positive
            elif b_i < b_o and a_i > a_o:
                angle_corrector = math.atan(a_from_origin / b_from_origin) + (1.5 * pi)

            else:
                angle_corrector = 0
                


            # Calculate the point's rotated value
            a_f = radius * math.cos(rads+angle_corrector) + a_o
            b_f = radius * math.sin(rads+angle_corrector) + b_o

            # Update shape
            point[axes[0]] = a_f
            point[axes[1]] = b_f