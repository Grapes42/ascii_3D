import numpy as np
import cv2

from data_types import *

class Projection():
    def __init__(self, fx=800, fy=800, cx=0, cy=0, screen_height=50, screen_width=100, scale=1) -> None:
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.scale = scale

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

    def map_to_2d(self, points_3d):
        # Map 3D points to a 2D plane
        points_2d, _ = cv2.projectPoints(points_3d,
                                        self.rvec, self.tvec,
                                        self.camera_matrix,
                                        self.dist_coeffs)
        points = []

        for i in range(len(points_2d)):
            points.append(Coord_2D(
                            points_2d[i,0,0]+(self.screen_height/2), 
                            points_2d[i,0,1]+(self.screen_width/2)
                        ))
            
        return points


    def cube_by_center(self, origin, width=1, height=1, depth=1):

        width *= self.scale
        height *= self.scale
        depth *= self.scale

        origin.y *= self.scale
        origin.x *= self.scale
        origin.z *= self.scale

        print(width)

        points_3d = np.array([[     [origin.y-(height/2), origin.x-(width/2), origin.z-(depth/2)], # Top left front
                                    [origin.y+(height/2), origin.x-(width/2), origin.z-(depth/2)], # Bottom left front
                                    [origin.y-(height/2), origin.x+(width/2), origin.z-(depth/2)], # Top right front
                                    [origin.y+(height/2), origin.x+(width/2), origin.z-(depth/2)], # Bottom right front
                                    
                                    [origin.y-(height/2), origin.x-(width/2), origin.z+(depth/2)], # Top left back
                                    [origin.y+(height/2), origin.x-(width/2), origin.z+(depth/2)], # Bottom left back
                                    [origin.y-(height/2), origin.x+(width/2), origin.z+(depth/2)], # Top right back
                                    [origin.y+(height/2), origin.x+(width/2), origin.z+(depth/2)]  # Bottom right back    
                            ]], np.float32)
        
        pairs = [ [0, 1], [1, 3], [3, 2], [2, 0],
                  [4, 5], [5, 7], [7, 6], [6, 4],
                  [0, 4], [1, 5], [3, 7], [2, 6] ]

        return self.map_to_2d(points_3d), pairs


    def cube_by_corners(self, coord0, coord1):
        points_3d = np.array([[     [coord0.y, coord0.x, coord0.z], # Coord0                0
                                    [coord1.y, coord0.x, coord0.z], # Coord0, Coord1 y      1
                                    [coord0.y, coord1.x, coord0.z], # Coord0, Coord1 x      2
                                    [coord0.y, coord0.x, coord1.z], # Coord0, Coord1 z      3

                                    [coord1.y, coord1.x, coord1.z], # Coord 1               4
                                    [coord0.y, coord1.x, coord1.z], # Coord 1, Coord0 y     5
                                    [coord1.y, coord0.x, coord1.z], # Coord 1, Coord0 x     6
                                    [coord1.y, coord1.x, coord0.z], # Coord 1, Coord0 z     7
                            ]], np.float32)
        
        pairs = [ [0, 2], [2, 7], [7, 1], [1, 0],
                  [3, 5], [5, 4], [4, 6], [6, 3],
                  [0, 3], [2, 5], [7, 4], [1, 6] ]
        
        return self.map_to_2d(points_3d), pairs
    