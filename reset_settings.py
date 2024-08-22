import os

settings = """# Visual Settings

screen_height: 80
screen_width: 150

font: "Monospace"
font_size: 12

fps: 60
fov: 90

fg_color: "#b6f2d8"
bg_color: "#131e19"


# Control Settings

sensitivity: 1
movement_speed: 0.1

bullet_speed: 1"""

with open("settings.eth", "w") as f:
    f.write(settings)