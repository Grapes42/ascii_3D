"""
File: main.py

Usage: Relates all programs together to work as a cohesive entity.
"""

import time
import os
from os import name

# Local imports
from shapes import *
from projection import Projection
from object_3D import *
from graphing import Graphing
from interface import Interface

# Constants
Y = 0
X = 1
Z = 2

LEFT = 0
MIDDLE = 1
RIGHT = 2

pi = 3.14159265359

# Paths
settings_path = "settings.txt"
pistol_path = "code/ascii_art/pistol.eth"



# Main functions
def construct(objects) -> None:
    for object in objects:
        points, pairs, z_map = projection.map_to_2d(object.array, object.pairs)
        graphing.construct_pairs(points=points, pairs=pairs, step_size=1, char=object.char)
        
def move(objects, axis, amount) -> None:
    for object in objects:
        object.move(axis=axis, amount=amount)
    
def rotate(objects, axis, amount) -> None:
    for object in objects:
        object.rotate(origin=[0, 0, 0], rads=amount, axis=axis)

def grab_art(file) -> list:
    final_lines = []
    with open(file) as f:
        lines = f.readlines()

        for line in lines:
            final_lines.append(line.replace("\n", ""))
    
    return final_lines



# Settings from file
settings = {}

with open(settings_path) as f:
    for line in f:
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        if line != "":
            if line[0] != "#":
                parts = line.split(":")
                name = parts[0]
                value = parts[1]

                if "\"" in value:
                    value = value.replace("\"", "")
                elif "." in value:
                    value = float(value)
                else:
                    value = int(value)

                settings[name] = value

screen_height = settings["screen_height"]
screen_width = settings["screen_width"]

font = settings["font"]
font_size = settings["font_size"]
line_spacing = font_size

fps = settings["fps"]
time_per_frame = 1/fps

fov = settings["fov"]

fg_color = settings["fg_color"]
bg_color = settings["bg_color"]

sens = settings["sensitivity"]
move_speed = settings["movement_speed"]

bullet_speed = settings["bullet_speed"]



# Sprites
pistol_lines = grab_art(pistol_path)




# Defining objects
y_correction = .7

# Defining the object for graphing
graphing = Graphing(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2),
                y_correction=y_correction)

# Defining the object for the interface
interface = Interface(chars_height=screen_height, chars_width=screen_width,
                font_size=font_size, font=font, line_spacing=line_spacing,
                fg_color=fg_color, bg_color=bg_color)

# Defining the object for projection
projection = Projection(fy=fov, fx=fov, height=screen_height, width=screen_width, y_correction=y_correction)



# Creating 3D objects
objects = []
bullets = []
background = []

# Test shapes

# Cube
cube = Object3D(center=[0,0,3], char=".")
cube.array, cube.pairs, cube.faces = cube_by_center(center=cube.center,
                                                    height=1, width=1, depth=1)
objects.append(cube)

cube1 = Object3D(center=[0,0,6], char=".")
cube1.array, cube1.pairs, cube1.faces = cube_by_center(center=cube1.center,
                                                       height=1, width=1, depth=1)
objects.append(cube1)


# Info text
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

controls_text = f"""Movement Speed: {move_speed}
Look Sensitivity: {sens}

Move: WASD
Look: Mouse Movement
Shoot: Left Click
Spawn Cube: Right Click
Exit: ESC"""

info_text_lines = info_text.split("\n")



# Controls text
controls_text_lines = controls_text.split("\n")
controls_text_y = screen_height - interface.border - len(controls_text_lines)

pistol_y = screen_height - len(pistol_lines)
pistol_x = screen_width/2 - 20

rads_from_horizon = 0



# Startup Screen
interface.startup_screen()



# Main loop
interface.setup_game_window()

object_placed = False

while True:
    # Construct world by projecting all points and drawing paths between all pairs
    world = objects + bullets
    construct(world)
    construct(background)
    

    # HUD

    # Crosshair
    graphing.plot(y=0, x=0, char="+")

    # Border
    graphing.rectangle(coord0=[0, 0],
                       coord1=[screen_height-1, screen_width-1],
                       char=".", y_correction=False, add_origin=False)



    # Drawing texts and sprites

    # Info text
    text_y = 0
    for line in info_text_lines:
        graphing.write(y=text_y, x=2, message=line, add_origin=False)
        text_y += 1

    # Controls text
    text_y = controls_text_y
    for line in controls_text_lines:
        graphing.write(y=text_y, x=2, message=line, add_origin=False)
        text_y += 1

    # Pistol
    text_y = pistol_y
    for line in pistol_lines:
        graphing.write(y=text_y, x=pistol_x, message=line, add_origin=False, gap_char="|")
        text_y += 1
    


    # Inputs
    move_dir, mouse_dir, mouse_buttons = interface.update(graphing.array)



    # Looking
    if mouse_dir[X] != 0:
        if rads_from_horizon != 0:
            rotate(world, axis=X, amount=-rads_from_horizon)
            rotate(background, axis=X, amount=-rads_from_horizon)

            rotate(world, axis=Y, amount=mouse_dir[X]*sens)
            rotate(background, axis=Y, amount=mouse_dir[X]*sens)

            rotate(world, axis=X, amount=rads_from_horizon)
            rotate(background, axis=X, amount=rads_from_horizon)
        else:
            rotate(world, axis=Y, amount=mouse_dir[X]*sens)
            rotate(background, axis=Y, amount=mouse_dir[X]*sens)

    if mouse_dir[Y] != 0:
        at_up_limit = (rads_from_horizon <= -pi/2) and (mouse_dir[Y] < 0)
        at_down_limit = (rads_from_horizon >= pi/2) and (mouse_dir[Y] > 0)


        if not at_up_limit and not at_down_limit:
            vert_amount = mouse_dir[Y] * sens

            rotate(world, axis=X, amount=vert_amount)
            rotate(background, axis=X, amount=vert_amount)

            rads_from_horizon += vert_amount



    # Movement    
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

    if mouse_buttons[RIGHT] == 0:
        object_placed = False

    elif mouse_buttons[RIGHT] == 1 and not object_placed:
        cube = Object3D(char="+")
        cube.array, cube.pairs = cube_by_center(x=0, y=0, z=2,
                                                height=.5, width=.5, depth=.5)
        objects.append(cube)

        object_placed = True


    # Move all bullets forward, and destroy them if they are 10 units away from the player
    for bullet in bullets:
        bullet.move(axis=Z, amount=bullet_speed)

        if bullet.array[0, 0, Z] > 10:
            bullets.remove(bullet)

    # Rotate with new system test
    #cube.rotate(origin=cube.center, axis=Z, rads=.2)
    #print(cube.center)

    # Wait as per the framerate
    time.sleep(time_per_frame)

    # Resets the 2D graph
    graphing.clear()

            