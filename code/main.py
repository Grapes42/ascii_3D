import time
import sys

# Local imports
from shapes import *
from projection import Projection
from object_3D import *
from graphing import Graphing
from interface import Interface

Y = 0
X = 1
Z = 2

LEFT = 0
MIDDLE = 1
RIGHT = 2

pi = 3.14159265359

screen_height = 80
screen_width = 150

font = "Monospace"
font_size = 12

line_spacing = font_size

fps = 60
time_per_frame = 1/60

fov = 90




def construct(objects):
    for object in objects:
        points, pairs = projection.map_to_2d(object.array, object.pairs)
        graphing.construct_pairs(points=points, pairs=pairs, step_size=1, char=object.char)
        
def move(objects, axis, amount):
    for object in objects:
        object.move(axis=axis, amount=amount)
    
def rotate(objects, axis, amount):
    for object in objects:
        object.rotate(origin=[0, 0, 0], rads=amount, axis=axis)

fg_color = [182,242,216]
bg_color=[19,30,25]

for i in range(len(sys.argv)):
    if sys.argv[i] == "-fg":
        parts = sys.argv[i+1].split(",")

        fg_color = [int(parts[0]),int(parts[1]),int(parts[2])]

    elif sys.argv[i] == "-bg":
        parts = sys.argv[i+1].split(",")

        bg_color = [int(parts[0]),int(parts[1]),int(parts[2])]

# Defining the object for graphing
graphing = Graphing(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2),
                y_correction=.7)

# Defining the object for the interface
interface = Interface(chars_height=screen_height, chars_width=screen_width,
                font_size=font_size, font=font, line_spacing=line_spacing,
                fg_color=fg_color, bg_color=bg_color)

# Defining the object for projection
projection = Projection(fy=fov, fx=fov, height=screen_height, width=screen_width)



#
# Creating 3D objects
#
objects = []
bullets = []

# Test shapes
cube = Object3D(char=".")
cube.array, cube.pairs = cube_by_center(x=0, y=0, z=5,
                                        height=1, width=1, depth=1)
objects.append(cube)

cube1 = Object3D(char="~")
cube1.array, cube1.pairs = cube_by_center(x=-1.2, y=.4, z=6,
                                        height=.2, width=1, depth=1)
objects.append(cube1)


pyramid = Object3D(char="*")
pyramid.array, pyramid.pairs = pyramid_by_center(x=1, y=-.5, z=7,
                                        height=2, width=1, depth=1)
objects.append(pyramid)

cube = Object3D(char="+")
cube.array, cube.pairs = cube_by_center(x=2, y=0, z=-2,
                                        height=1, width=1, depth=1)
objects.append(cube)

cube = Object3D(char="#")
cube.array, cube.pairs = cube_by_center(x=-2, y=0, z=0,
                                        height=1, width=2, depth=2)
objects.append(cube)

#cube.rotate(origin=[0, 0, 10], rads=.4, axis=Z)
#cube.rotate(origin=[0, 0, 10], rads=.5, axis=X)




# Info message
info_text = f"""
 ____             _   _     
|  _ \ _   _  ___| |_| |__  
| |_) | | | |/ _ \ __| '_ \ 
|  __/| |_| |  __/ |_| | | |
|_|    \__, |\___|\__|_| |_|
       |___/

by Max Dowdall

Character Array: {interface.chars_width} x {interface.chars_height}
Window: {interface.pixel_width}px x {interface.pixel_height}px
Font: {interface.font_selector}, size {interface.font_size}
FOV: {fov}
FPS: {fps}
"""

pistol = """|||||||||||||||||||:*:||||||||||||||||||||||||||||
|||||||||||||||||.,,:,.|||||||||||||||||||||||||||
|||||||||||||||.+=++**+,.|||||||||||||||||||||||||
||||||||||||||.++,**=++:..||||||||||||||||||||||||
||||||||||||||.::,+=#=+,,,||||||||||||||||||||||||
||||||||||||||.:+*###==:::||||||||||||||||||||||||
||||||||||||||.:*==##==+++,|||||||||||||||||||||||
|||||||||||||.+==#====+==+:.||||||||||||||||||||||
|||||||||||:++*###==+::+++++,|||||||||||||||||||||
||||||||:*=##==#W##=+::,,:+===+.||||||||||||||||||
||||||||.,:#=+=W##==*++,. :+::,+||||||||||||||||||
||||||||,+::+:=#==:..   .  ,::..||||||||||||||||||
|||||||||.++++#=*,        .::+||||||||||||||||||||
|||||||||:++++W=*+::.    ,:+,:.:=*:|||||||||||||||
|||||||||++*+:=====+:,,::++:.,.:====.|||||||||||||
|||||,:::::,,+*+: . .    ....:==#####==+.|||||||||
|||:======#==*:==+=:+,,....*==########===+||||||||
||:===####W@@@##==**+*===##WW##########==*||||||||
|.+=++=###W@WWW######==######==########==+:|||||||
|,+:.:===##################==####========+==:|||||
||.:::*===#######WWW#########==========*+:+=:|||||
|||||:++===###==##=##########==#========+:,,||||||
|||||...:+=====+=====#############==####=++,||||||
|||||||||,:+*======########======####==#=+:|||||||
|||||||||.|.:++:+========######WWW#####===+|||||||
||||||||||.|.,:*=+*==#====#######========#==+.||||
||||||||||..||:,+=##=###===###WW##==========+::+:|
"""

info_text_lines = info_text.split("\n")
pistol_lines = pistol.split("\n")
pistol_y = screen_height - len(pistol_lines)
pistol_x = screen_width/2 - 20

rads_from_horizon = 0

#
# Various Centers
#

# Control Parameters
sens = 1
move_speed = .1

bullet_speed = .5
bullet_shot = True

move_dir = [0, 0]


#
# Main loop
#
while True:
    world = objects + bullets

    construct(world)
    

    #
    # HUD
    #

    # Crosshair
    graphing.plot(y=0, x=0, char="+")

    # Border
    graphing.rectangle(coord0=[0, 0],
                       coord1=[screen_height-1, screen_width-1],
                       char=".", y_correction=False, add_origin=False)


    text_y = 0
    for line in info_text_lines:
        graphing.write(y=text_y, x=2, message=line, add_origin=False)
        text_y += 1

    text_y = pistol_y
    for line in pistol_lines:
        graphing.write(y=text_y, x=pistol_x, message=line, add_origin=False, gap_char="|")
        text_y += 1
    
    #
    # Movement
    #
    move_dir, mouse_dir, mouse_buttons = interface.update(graphing.array)

    # Looking
    if mouse_dir[X] != 0:
        if rads_from_horizon != 0:
            rotate(world, axis=X, amount=-rads_from_horizon)

            rotate(world, axis=Y, amount=mouse_dir[X]*sens)

            rotate(world, axis=X, amount=rads_from_horizon)
        else:
            rotate(world, axis=Y, amount=mouse_dir[X]*sens)

    if mouse_dir[Y] != 0:
        vert_amount = mouse_dir[Y] * sens

        rotate(world, axis=X, amount=vert_amount)

        rads_from_horizon += vert_amount

    # Turning
    if move_dir[X] != 0:
        move(world, axis=X, amount=move_dir[X]*move_speed)

    if move_dir[Y] != 0:
        if rads_from_horizon != 0:
            rotate(world, axis=X, amount=-rads_from_horizon)
            move(world, axis=Z, amount=move_dir[Y]*move_speed)
            rotate(world, axis=X, amount=rads_from_horizon)
        else:
            move(world, axis=Z, amount=move_dir[Y]*move_speed)

    # Mouse buttons
    if mouse_buttons[LEFT] == 0:
        bullet_shot = False

    elif mouse_buttons[LEFT] == 1 and not bullet_shot:
        bullet = Object3D(char=".")
        bullet.array, bullet.pairs = cube_by_center(x=0, y=0, z=1,
                                                height=.2, width=.2, depth=.2)
        bullets.append(bullet)

        bullet_shot = True


    for bullet in bullets:
        bullet.move(axis=Z, amount=bullet_speed)

        if bullet.array[0, 0, Z] > 10:
            bullets.remove(bullet)

    time.sleep(time_per_frame)

    # Resets the 2D graph
    graphing.clear()

            