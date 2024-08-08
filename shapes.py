import numpy as np

def cube_by_center(y=0, x=0, z=0, width=1, height=1, depth=1):
        points_3d = np.array([[     [y-(height/2), x-(width/2), z-(depth/2)], # Top left front
                                    [y+(height/2), x-(width/2), z-(depth/2)], # Bottom left front
                                    [y-(height/2), x+(width/2), z-(depth/2)], # Top right front
                                    [y+(height/2), x+(width/2), z-(depth/2)], # Bottom right front
                                    
                                    [y-(height/2), x-(width/2), z+(depth/2)], # Top left back
                                    [y+(height/2), x-(width/2), z+(depth/2)], # Bottom left back
                                    [y-(height/2), x+(width/2), z+(depth/2)], # Top right back
                                    [y+(height/2), x+(width/2), z+(depth/2)]  # Bottom right back    
                            ]], np.float32)
        
        pairs = [ [0, 1], [1, 3], [3, 2], [2, 0],
                  [4, 5], [5, 7], [7, 6], [6, 4],
                  [0, 4], [1, 5], [3, 7], [2, 6] ]
        
        return points_3d, pairs