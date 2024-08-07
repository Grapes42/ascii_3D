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

        
screen = Screen(height=40, width=40)

points = [Coord(0,0), Coord(0, 10), Coord(15,0), Coord(10,20)]


pairs = [[0,1], [1,3], [3,2], [2,0]]

screen.construct_pairs(points=points, pairs=pairs, step_size=.5)

screen.print()