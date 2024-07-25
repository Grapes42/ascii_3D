from os import system, name

class Screen():
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.arr = [[" " for x in range(self.width)] for y in range(self.height)]

    def plot(self, coord, char):
        self.arr[round(coord.y)][round(coord.x)] = char

    def print(self):
        screen_str = ""
        for y in range(len(self.arr)):
            line = ""
            for x in range(len(self.arr[0])):
                line += str(self.arr[y][x])
            screen_str += f"{line}\n"

        #self.clear()
        print(screen_str)

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

class Coord():
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __str__(self) -> str:
        return f"y: {self.y}, x: {self.x}"

        
screen = Screen(height=25, width=25)

def line(coord0, coord1, step_size=1):
    rise = coord0.x - coord1.x
    run = coord0.y - coord1.y

    if rise != 0:
        gradient = run/rise

        if coord0.x <= coord1.x:
            pos = coord0
            end = coord1
        else:
            pos = coord1
            end = coord0

        while pos.x <= end.x:
            screen.plot(pos, char="#")
            pos.x += step_size
            pos.y += gradient*step_size
    
    else:
        if coord0.y <= coord1.y:
            pos = coord0
            end = coord1
        else:
            pos = coord1
            end = coord0

        while pos.y <= end.y:
            screen.plot(pos, "#")
            pos.y += step_size


    



a = Coord(10,0)
b = Coord(0, 10)

screen.plot(a, "s")
screen.plot(b, "e")

line(a, b, .5)
line(Coord(0, 0), Coord(15, 10), .5)
line(Coord(10, 10), Coord(0, 10))

screen.print()