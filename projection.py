import numpy as np
import cv2

class Projection():
    def __init__(self, fx=800, fy=800, cx=0, cy=0) -> None:

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

        return points_2d
            
