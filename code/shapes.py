"""
File: shapes.py

Usage: Provides presets for regular shapes.
"""

import numpy as np

Y = 0
X = 1
Z = 2

def cube_by_center(center, width=1, height=1, depth=1) -> {list, list}:
        y = center[Y]
        x = center[X]
        z = center[Z]
        
        points_3d = np.array([[     
                [y-(height/2), x-(width/2), z-(depth/2)], # 0, Top left front
                [y+(height/2), x-(width/2), z-(depth/2)], # 1, Bottom left front
                [y-(height/2), x+(width/2), z-(depth/2)], # 2, Top right front
                [y+(height/2), x+(width/2), z-(depth/2)], # 3, Bottom right front
                
                [y-(height/2), x-(width/2), z+(depth/2)], # 4, Top left back
                [y+(height/2), x-(width/2), z+(depth/2)], # 5, Bottom left back
                [y-(height/2), x+(width/2), z+(depth/2)], # 6, Top right back
                [y+(height/2), x+(width/2), z+(depth/2)]  # 7, Bottom right back    
        ]], np.float32)
        
        pairs = [ 
                [0, 1], [1, 3], [3, 2], [2, 0],
                [4, 5], [5, 7], [7, 6], [6, 4],
                [0, 4], [1, 5], [3, 7], [2, 6] 
        ]

        faces = [
                [0, 1, 3, 2], # Front face
                [4, 5, 7, 6], # Back face
                [0, 1, 5, 4], # Left face
                [2, 3, 7, 6], # Right face
                [0, 2, 6, 4], # Top face
                [1, 3, 7, 5], # Bottom face
        ]
        
        return points_3d, pairs, faces

""" i'll do this later lol
def dodecahedron_by_center(y=0, x=0, z=0):
        h = 
        0, +-(1+h), +-(1-h^2)

        +-(1+h), +-(1-h^2), 0

        +-(1-h^2), 0, +-(1+h)

        points_3d = np.array([[         
                                []
                            ]])
"""

def pyramid_by_center(y=0, x=0, z=0, width=1, height=1, depth=1) -> {list, list}:
        points_3d = np.array([[
                [y+(height/2), x-(width/2), z-(depth/2)],
                [y+(height/2), x+(width/2), z-(depth/2)],
                [y+(height/2), x-(width/2), z+(depth/2)],
                [y+(height/2), x+(width/2), z+(depth/2)],
                [y-(height/2), x, z]
        ]])

        pairs = [
                [0, 1], [1, 3], [3, 2], [2, 0],
                [0, 4], [1, 4], [2, 4], [3, 4] 
        ]

        return points_3d, pairs



def cube_by_corners(x0, y0, z0, x1, y1, z1) -> {list, list}:
        points_3d = np.array([[     
                [y0, x0, z0], # Coord0                0
                [y1, x0, z0], # Coord0, Coord1 y      1
                [y0, x1, z0], # Coord0, Coord1 x      2
                [y0, x0, z1], # Coord0, Coord1 z      3

                [y1, x1, z1], # Coord 1               4
                [y0, x1, z1], # Coord 1, Coord0 y     5
                [y1, x0, z1], # Coord 1, Coord0 x     6
                [y1, x1, z0], # Coord 1, Coord0 z     7
        ]], np.float32)
        
        pairs = [ 
                [0, 2], [2, 7], [7, 1], [1, 0],
                [3, 5], [5, 4], [4, 6], [6, 3],
                [0, 3], [2, 5], [7, 4], [1, 6] 
        ]
        
        return points_3d, pairs

