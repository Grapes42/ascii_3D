settings = """# Visual Settings

screen_height: 80
screen_width: 150

font: "Monospace"
font_size: 12

fps: 60
fov: 90

fg_color: "#b6f2d8"
bg_color: "#131e19"

# Below are some nice pallets from lospec.com to try 
# (just replace the color values above with the colors
# of your choice)

# Station Defender by Calvino Sinclair: 
# fg_color: "#a692b0"
# bg_color: "#17141c"

# 1Bit Monitor Glow by Polyducks:
# fg_color: "#f0f6f0"
# bg_color: "#222323"

# Pixel Ink by Polyducks:
# fg_color: "#edf6d6" 
# bg_color: "#3e232c"

# Gato Roboto - Virtual Cat by PureAsbestos:
# fg_color: "#cc0e13"
# bg_color: "#2b0000"


# Control Settings

sensitivity: 1
movement_speed: 0.1

bullet_speed: 1"""

with open("settings.txt", "w") as f:
    f.write(settings)