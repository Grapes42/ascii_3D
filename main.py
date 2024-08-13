import tcod
import time

from shapes import *
from projection import Projection
from object_3D import *
from graphing import Graphing


Y = 0
X = 1
Z = 2

screen_height = 150
screen_width = 150

def construct_objects(objects):
    for object in objects:
        graphing.construct_pairs(points=projection.map_to_2d(object.array),
                               pairs=object.pairs)

graphing = Graphing(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2))

projection = Projection()

#
# Creating 3D objects
#
objects = []

# Test cube
cube = Object3D()
cube.array, cube.pairs = cube_by_center(x=0, y=0, z=10,
                                        height=1, width=1, depth=1)
objects.append(cube)

print(objects[0])

construct_objects(objects)


tileset = tcod.tileset.load_tilesheet(
    "chars.png", 32, 8, tcod.tileset.CHARMAP_TCOD
)

with tcod.context.new_terminal(
    screen_width,
    screen_height,
    tileset=tileset,
    title="Ascii 3D",
    vsync=True,
) as context:
    root_console = tcod.Console(screen_width, screen_height, order="F")
    while True:

        for y in range(len(graphing.array)):
            for x in range(len(graphing.array[0])):
                root_console.print(x=x, y=y, string=graphing.array[y, x])

        graphing.clear()

        screen_str = ""
        for y in range(len(graphing.array)):
            line = ""
            for x in range(len(graphing.array[0])):
                line += str(graphing.array[y, x])
            screen_str += f"{line}\n"

        print(screen_str)

        cube.rotate(origin=[0,0,10], rads=.2, axis=Y)
        construct_objects(objects)
        time.sleep(.1)

        context.present(root_console)

        for event in tcod.event.wait():
            if event.type == "QUIT":
                raise SystemExit()
            