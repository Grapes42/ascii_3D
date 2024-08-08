class Coord_2D():
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __str__(self) -> str:
        return f"y: {self.y}, x: {self.x}"
    
class Coord_3D():
    def __init__(self, y, x, z) -> None:
        self.y = y
        self.x = x
        self.z = z

    def __str__(self) -> str:
        return f"y: {self.y}, x: {self.x}, z: {self.z}"