from screen import Screen

class Coord():
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __str__(self) -> str:
        return f"y: {self.y}, x: {self.x}"

        
screen = Screen(height=40, width=40)


a = Coord(10,0)
b = Coord(0, 10)

screen.plot(a, "s")
screen.plot(b, "e")

#screen.line(a, b, .5)
#screen.line(Coord(0, 0), Coord(15, 10), .5)
#screen.line(Coord(10, 10), Coord(0, 10))

screen.func(origin=Coord(15,15), func="**2/10")

screen.print()