import pygame

Y = 0
X = 1

LEFT = 0
MIDDLE = 1
RIGHT = 2

pi = 3.14159265359

class Interface():
    def __init__(self, chars_height, chars_width, border=2, font="Monospace", font_size=5, line_spacing=1, fg_color=(255,255,255), bg_color=(0,0,0)) -> None:
        # Sets the width and height of the character array
        self.chars_height = chars_height
        self.chars_width = chars_width

        # Sets the font and font size
        self.font_selector = font
        self.font_size = font_size

        # Sets the width and height of the window based on the font size and character array size
        self.border = border 

        self.pixel_height = round(line_spacing * (self.chars_height + border * 2)) # height based on line spacing * (no of rows + border)
        self.pixel_width = round((.6 * font_size) * (self.chars_width + border * 4)) # width based on magic number (will be improved later) * (no of columns + border)

        self.fg_color = fg_color
        self.bg_color = bg_color

        # PyGame window setup
        pygame.init()

        pygame.font.init()
        pygame.font.get_init()

        pygame.mouse.set_visible(False)
        
        self.display_surface = pygame.display.set_mode((self.pixel_width, self.pixel_height))
        
        pygame.display.set_caption("Ascii 3D")

        self.font = pygame.font.SysFont(self.font_selector, font_size)

        # Defining the blank screen rows
        self.rendered_rows = []

        for y in range(self.chars_height):
            self.rendered_rows.append(self.font.render("#"*chars_width, True, self.fg_color))

        # Defining the rectangles for the rows to sit in
        self.rectangles = []

        y_pos = line_spacing * border

        for y in range(self.chars_height):
            self.rectangles.append(self.rendered_rows[y].get_rect())

            self.rectangles[y].center = (self.pixel_width/2,y_pos)

            y_pos += line_spacing

        
        # Controls variables
        self.mouse_dir = [0, 0]
        self.mouse_buttons = [0, 0, 0]

        self.move_dir = [0, 0]


    def update(self, array):
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

        for y in range(self.chars_height):
            self.display_surface.blit(self.rendered_rows[y], self.rectangles[y])


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
            
                # deactivating the pygame library
                pygame.quit()
    
                # quitting the program.
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                # Move
                elif event.key == pygame.K_w: 
                    self.move_dir[Y] -= 1
                elif event.key == pygame.K_s: 
                    self.move_dir[Y] += 1
                elif event.key == pygame.K_a: 
                    self.move_dir[X] += 1
                elif event.key == pygame.K_d: 
                    self.move_dir[X] -= 1

            elif event.type == pygame.KEYUP:
                # Move
                if event.key == pygame.K_w: 
                    self.move_dir[Y] += 1
                elif event.key == pygame.K_s: 
                    self.move_dir[Y] -= 1
                elif event.key == pygame.K_a: 
                    self.move_dir[X] -= 1
                elif event.key == pygame.K_d: 
                    self.move_dir[X] += 1
           
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_dir[X] = event.rel[0] * (2 * pi) / self.display_surface.get_width()
                self.mouse_dir[Y] = event.rel[1] * (2 * pi) / self.display_surface.get_width()
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
            

    
        # update the display
        pygame.display.update()

        return self.move_dir, self.mouse_dir, self.mouse_buttons