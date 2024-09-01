"""
File: projection.py

Usage: Handles all the logic of projecting 3D points in space to a 2D screen.
"""

import numpy as np
import cv2
from copy import copy

# Constants
Y = 0
X = 1
Z = 2

class Projection():
    def __init__(self, height, width, y_correction, fx=800, fy=800, cx=0, cy=0) -> None:

        # Sets the height and width of the character array
        self.height = height
        self.width = width

        self.y_correction = y_correction

        # Camera matrix
        self.camera_matrix = np.array([  
            [fx, 0, cx],
            [0, fy, cy],
            [0, 0, 1]], np.float32
        )

        # Distortion coeffectients
        self.dist_coeffs = np.zeros((5, 1), np.float32)

        # Rotation and translation vectors
        self.rvec = np.zeros((3, 1), np.float32)
        self.tvec = np.zeros((3, 1), np.float32)

        # Goals to do this projection maths from scratch



    def map_to_2d(self, points_3d, pairs) -> {list, list}:
        points_3d = copy(points_3d)

        # Define boundaries of the projection
        y_bound = self.height*self.y_correction
        x_bound = self.width/2

        pairs_for_projection = []

        object_on_screen = False

        # Remove all pairs behind the camera
        for pair in pairs:
            coord0 = points_3d[0, pair[0]]
            coord1 = points_3d[0, pair[1]]

            if coord0[Z] > 0 and coord1[Z] > 0:
                pairs_for_projection.append(pair)
                object_on_screen = True
            
        # If entire object is not on screen, skip
        if not object_on_screen:
            return [], []



        # Map 3D points to a 2D plane
        points_2d, _ = cv2.projectPoints(points_3d,
                                        self.rvec, self.tvec,
                                        self.camera_matrix,
                                        self.dist_coeffs)

        z_map = []

        for point in points_3d[0]:
            z_map.append(point[Z])
        
        pairs_for_rendering = []
        
        # Check each point to see if its on the screen
        for pair in pairs_for_projection:
            coord0_in_y_bound = points_2d[pair[0], 0, Y] > -y_bound and points_2d[pair[0], 0, Y] < y_bound
            coord0_in_x_bound = points_2d[pair[0], 0, X] > -x_bound and points_2d[pair[0], 0, X] < x_bound
            coord0_on_screen = coord0_in_y_bound and coord0_in_x_bound

            coord1_in_y_bound = points_2d[pair[1], 0, Y] > -y_bound and points_2d[pair[1], 0, Y] < y_bound
            coord1_in_x_bound = points_2d[pair[1], 0, X] > -x_bound and points_2d[pair[1], 0, X] < x_bound
            coord1_on_screen = coord1_in_y_bound and coord1_in_x_bound

            # If both points are on the screen, simply render it
            if coord0_on_screen and coord1_on_screen:
                pairs_for_rendering.append(pair)

        return points_2d, pairs_for_rendering, z_map
            
