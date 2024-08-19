import numpy as np
import cv2
from copy import copy

Y = 0
X = 1
Z = 2

class Projection():
    def __init__(self, height, width, fx=800, fy=800, cx=0, cy=0) -> None:

        self.height = height
        self.width = width

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


    def map_to_2d(self, points_3d, pairs):
        points_3d = copy(points_3d)
        y_bound = self.height
        x_bound = self.width

        pairs_for_projection = []

        object_on_screen = False

        for pair in pairs:
            coord0 = points_3d[0, pair[0]]
            coord1 = points_3d[0, pair[1]]

            if coord0[Z] > 0 or coord1[Z] > 0:
                pairs_for_projection.append(pair)
                object_on_screen = True
            


        if not object_on_screen:
            print("not rendered")
            return [], []


        # Map 3D points to a 2D plane
        points_2d, _ = cv2.projectPoints(points_3d,
                                        self.rvec, self.tvec,
                                        self.camera_matrix,
                                        self.dist_coeffs)
        
        pairs_for_rendering = []
        
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

        return points_2d, pairs_for_rendering
            
