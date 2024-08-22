"""
File: interface.py

Usage: Handles all input and output.
"""

import pygame

# Constants
Y = 0
X = 1

LEFT = 0
MIDDLE = 1
RIGHT = 2

pi = 3.14159265359

class Interface():
    def __init__(self, chars_height, chars_width, border=2, line_spacing=10, font="Monospace", font_size=5, fg_color=(255,255,255), bg_color=(0,0,0)) -> None:

        # Sets the width and height of the character array
        self.chars_height = chars_height
        self.chars_width = chars_width

        # Sets the font and font size
        self.font_selector = font
        self.font_size = font_size
        self.line_spacing = line_spacing

        self.border = border

        # Sets the width and height of the window based on the font size and character array size
        self.border = border 

        self.pixel_height = round(self.line_spacing * (self.chars_height + border * 2)) # height based on line spacing * (no of rows + border)
        self.pixel_width = round((.6 * font_size) * (self.chars_width + border * 4)) # width based on magic number (will be improved later) * (no of columns + border)

        self.fg_color = fg_color
        self.bg_color = bg_color

        self.rendered_rows = []
        self.rectangles = []



        # PyGame window setup
        pygame.init()

        pygame.font.init()
        pygame.font.get_init()

        pygame.mouse.set_visible(False)
        
        self.display_surface = pygame.display.set_mode((self.pixel_width, self.pixel_height))
        
        pygame.display.set_caption("Pyeth - by Max Dowdall")



    def startup_screen(self) -> None:

        # Sets the font and font size
        startup_font = pygame.font.SysFont(self.font_selector, 20)
        startup_spacing = 25

        startup_text = """
                                  +------+
 ____             _   _          /|     /|
|  _ \ _   _  ___| |_| |__      +-+----+ |
| |_) | | | |/ _ \ __| '_ \     | |    | |
|  __/| |_| |  __/ |_| | | |    | +----+ +
|_|    \__, |\___|\__|_| |_|    |/     |/ 
       |___/                    +------+  
       
An ASCII 3D rendering program by Max Dowdall.



What you will see next is an example of where the 
software currently is (as of 22/08/24).

I have many plans to use this program to create some 80's sci-fi-esque
games inspired by computer graphics in the likes of "Alien (1979)". 
And some 3D versions of classic rouguelikes like "Nethack".

Information about the current scene will be at the top left.

The controls will be at the bottom left.

Settings can by editing "settings.eth" and restarting the program.



Press any key to continue"""

        startup_lines = startup_text.split("\n")


        
        # Define blank lines to create rectangles
        for line in startup_lines:
            self.rendered_rows.append(startup_font.render(line, True, self.fg_color))

        y_pos = self.pixel_height/2 - (startup_spacing * len(self.rendered_rows) / 2)



        # Create rectangles
        for i in range(len(self.rendered_rows)):
            self.rectangles.append(self.rendered_rows[i].get_rect())

            self.rectangles[i].center = (self.pixel_width/2,y_pos)

            y_pos += startup_spacing



        # Adds background and text to the window
        self.display_surface.fill(self.bg_color)

        # Prints out all the characters
        for i in range(len(self.rendered_rows)):
            self.display_surface.blit(self.rendered_rows[i], self.rectangles[i])
        
        # Update the window
        pygame.display.update()



        # Check input events
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return


        
    def setup_game_window(self) -> None:

        # Reset rows and rectangles
        self.rendered_rows = []
        self.rectangles = []

        # Set font
        self.font = pygame.font.SysFont(self.font_selector, self.font_size)

        # Define blank lines to create rectangles
        for y in range(self.chars_height):
            self.rendered_rows.append(self.font.render(" "*self.chars_width, True, self.fg_color))

        y_pos = self.line_spacing * self.border



        # Create rectangles
        for y in range(self.chars_height):
            self.rectangles.append(self.rendered_rows[y].get_rect())

            self.rectangles[y].center = (self.pixel_width/2,y_pos)

            y_pos += self.line_spacing

        

        # Controls variables
        self.mouse_dir = [0, 0]
        self.mouse_buttons = [0, 0, 0]

        self.move_dir = [0, 0]



    def update(self, array) -> {list, list, list}:

        # Converts the character array into a list of row strings
        str_rows = []

        for y in range(len(array)):
            line = ""
            for x in range(len(array[0])):
                line += str(array[y, x])
            str_rows.append(line)



        # Renders each row and appends them to a list
        for y in range(self.chars_height):
            self.rendered_rows[y] = self.font.render(str_rows[y], True, self.fg_color)
        
        # Adds background and text to the window
        self.display_surface.fill(self.bg_color)

        # Prints out all the characters
        for y in range(self.chars_height):
            self.display_surface.blit(self.rendered_rows[y], self.rectangles[y])



        # Checks input events
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("\n\nThanks for testing out Pyeth!")
                    print("More info about the project can be found at https://github.com/Grapes42/pyeth")

                    pygame.quit()
                    quit()

                # Movement
                elif event.key == pygame.K_w: 
                    self.move_dir[Y] -= 1
                elif event.key == pygame.K_s: 
                    self.move_dir[Y] += 1
                elif event.key == pygame.K_a: 
                    self.move_dir[X] += 1
                elif event.key == pygame.K_d: 
                    self.move_dir[X] -= 1

            elif event.type == pygame.KEYUP:
                # Movement
                if event.key == pygame.K_w: 
                    self.move_dir[Y] += 1
                elif event.key == pygame.K_s: 
                    self.move_dir[Y] -= 1
                elif event.key == pygame.K_a: 
                    self.move_dir[X] -= 1
                elif event.key == pygame.K_d: 
                    self.move_dir[X] += 1
           
            elif event.type == pygame.MOUSEMOTION:
                # Add the mouse x and y velocities to the mouse motion list
                self.mouse_dir[X] = event.rel[0] * (2 * pi) / self.display_surface.get_width()
                self.mouse_dir[Y] = event.rel[1] * (2 * pi) / self.display_surface.get_width()

                # Move the mouse back to the center of the window
                pygame.mouse.set_pos(self.display_surface.get_rect().center)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_buttons[LEFT] = 1
                elif event.button == 2:
                    self.mouse_buttons[MIDDLE] = 1
                elif event.button == 3:
                    self.mouse_buttons[RIGHT] = 1

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_buttons[LEFT] = 0
                elif event.button == 2:
                    self.mouse_buttons[MIDDLE] = 0
                elif event.button == 3:
                    self.mouse_buttons[RIGHT] = 0
            

    
        # Update the window
        pygame.display.update()

        return self.move_dir, self.mouse_dir, self.mouse_buttons