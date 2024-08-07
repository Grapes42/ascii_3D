import numpy as np
import cv2

from screen import Screen

class Coord():
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __str__(self) -> str:
        return f"y: {self.y}, x: {self.x}"
    
class Pair():
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

screen = Screen(height=round(1080/10), width=round(1920/10))

# Defining the camera matrix
fx = 800
fy = 800
cx = 640
cy = 480
camera_matrix = np.array([[fx, 0, cx],
                          [0, fy, cy],
                          [0, 0, 1]], np.float32)

# Defining the distortion coeffectients
dist_coeffs = np.zeros((5, 1), np.float32)

# Defining the 3D point in the world
x, y, z = 10, 20, 30
points_3d = np.array([[[x, y-10, z], [x, y+10, z], [x, y-10, z-5], [x, y+10, z-5]]], np.float32)

# Define the rotation and translation vectors
rvec = np.zeros((3, 1), np.float32)
tvec = np.zeros((3, 1), np.float32)

# Map the 3D point to a 2D point
points_2d, _ = cv2.projectPoints(points_3d,
                                rvec, tvec,
                                camera_matrix,
                                dist_coeffs)

print(points_2d)

points = []

for i in range(len(points_2d)):
    points.append(Coord(points_2d[i,0,0]/10, points_2d[i,0,1]/10))

for point in points:
    screen.plot(point)

#points = [Coord(0,0), Coord(0, 10), Coord(15,0), Coord(10,20)]

#pairs = [[0,1], [1,3], [3,2], [2,0]]

#screen.construct_pairs(points=points, pairs=pairs, step_size=.5)

screen.print()