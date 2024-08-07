from os import system, name
from copy import copy

class Screen():
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.arr = [[" " for x in range(self.width)] for y in range(self.height)]

    def plot(self, coord, char="#"):
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

    def line(self, coord0, coord1, step_size=1):
        rise = coord0.x - coord1.x
        run = coord0.y - coord1.y

        if rise != 0:
            gradient = run/rise

            if coord0.x <= coord1.x:
                pos = copy(coord0)
                end = copy(coord1)
            else:
                pos = copy(coord1)
                end = copy(coord0)

            while pos.x <= end.x:
                self.plot(pos, char="#")
                pos.x += step_size
                pos.y += gradient*step_size
        
        else:
            if coord0.y <= coord1.y:
                pos = copy(coord0)
                end = copy(coord1)
            else:
                pos = copy(coord1)
                end = copy(coord0)

            while pos.y <= end.y:
                self.plot(pos, "#")
                pos.y += step_size

    def construct_pairs(self, points, pairs, step_size=1):
        for pair in pairs:
            self.line(points[pair[0]], points[pair[1]], step_size)


    def triangle(self, coord0, coord1, coord2):
        self.line(coord0, coord1)
        self.line(coord1, coord2)
        self.line(coord2, coord0)