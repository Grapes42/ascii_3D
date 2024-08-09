from shapes import *
from projection import Projection
from data_types import *
from screen import Screen

screen_height = 150
screen_width = 300

def construct_objects(objects):
    for object in objects:
        screen.construct_pairs(points=projection.map_to_2d(object.array),
                               pairs=object.pairs)

screen = Screen(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2))

projection = Projection()


objects = []

hall = Object3D()
hall.array, hall.pairs = cube_by_corners(x0=-1, y0=-.5, z0=5,
                                        x1=1, y1=.5, z1=20)
objects.append(hall)

door = Object3D()
door.array, door.pairs = cube_by_corners(x0=-.5, y0=-.25, z0=20,
                                        x1=.5, y1=.5, z1=30)
objects.append(door)

table = Object3D()
table.array, table.pairs = cube_by_corners(x0=.2, y0=.3, z0=7,
                                        x1=-1, y1=.5, z1=10)
objects.append(table)

table_item = Object3D()
table_item.array, table_item.pairs = cube_by_corners(x0=-.5, y0=.2, z0=8,
                                        x1=-1, y1=.3, z1=9)
objects.append(table_item)

shelf = Object3D()
shelf.array, shelf.pairs = cube_by_corners(x0=-.7, y0=-.18, z0=20,
                                        x1=-1, y1=-.15, z1=7)
objects.append(shelf)

pillar = Object3D()
pillar.array, pillar.pairs = cube_by_corners(x0=.5, y0=-.5, z0=12,
                                            x1=.8, y1=.5, z1=13)
objects.append(pillar)

pillar_1 = Object3D()
pillar_1.array, pillar_1.pairs = cube_by_corners(x0=.5, y0=-.5, z0=6,
                                            x1=.8, y1=.5, z1=7)
objects.append(pillar_1)


construct_objects(objects)

screen.print(clear=False)