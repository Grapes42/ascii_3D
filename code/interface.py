import pygame

Y = 0
X = 1

LEFT = 0
MIDDLE = 1
RIGHT = 2

class Interface():
    def __init__(self, chars_height, chars_width, pixel_height, pixel_width, frame_rate=60, font="Monospace", font_size=5, line_spacing=1, fg_color=(255,255,255), bg_color=(0,0,0)) -> None:
        # Setting a clock to control the frame rate
        self.clock = pygame.time.Clock()
        self.frame_rate = frame_rate
        
        # Sets the width and height of the character array
        self.chars_height = chars_height
        self.chars_width = chars_width

        # Style parameters
        self.font = font
        self.font_size = font_size

        self.fg_color = fg_color
        self.bg_color = bg_color

        # PyGame window setup
        pygame.font.init()
        pygame.font.get_init()
        
        self.display_surface = pygame.display.set_mode((pixel_width, pixel_height))
        
        pygame.display.set_caption("Ascii 3D")

        self.font = pygame.font.SysFont(font, font_size)

        # Defining the blank screen rows
        self.rendered_rows = []

        for y in range(self.chars_height):
            self.rendered_rows.append(self.font.render("#"*chars_width, True, self.fg_color))

        # Defining the rectangles for the rows to sit in
        self.rectangles = []

        y_pos = 0


        for y in range(self.chars_height):
            self.rectangles.append(self.rendered_rows[y].get_rect())

            self.rectangles[y].center = (round(pixel_width/2),y_pos)

            y_pos += line_spacing

        
        # Controls variables
        self.mouse_dir = [0, 0]
        self.mouse_buttons = [0, 0, 0]

        self.move_dir = [0, 0]
        self.turn_dir = [0, 0]



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
                # Move
                if event.key == pygame.K_w: 
                    self.move_dir[Y] -= 1
                elif event.key == pygame.K_s: 
                    self.move_dir[Y] += 1
                elif event.key == pygame.K_a: 
                    self.move_dir[X] += 1
                elif event.key == pygame.K_d: 
                    self.move_dir[X] -= 1

                # Turn
                elif event.key == pygame.K_UP: 
                    self.turn_dir[Y] -= 1
                elif event.key == pygame.K_DOWN: 
                    self.turn_dir[Y] += 1
                elif event.key == pygame.K_LEFT: 
                    self.turn_dir[X] -= 1
                elif event.key == pygame.K_RIGHT: 
                    self.turn_dir[X] += 1

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

                # Turn
                elif event.key == pygame.K_UP: 
                    self.turn_dir[Y] += 1
                elif event.key == pygame.K_DOWN: 
                    self.turn_dir[Y] -= 1
                elif event.key == pygame.K_LEFT: 
                    self.turn_dir[X] += 1
                elif event.key == pygame.K_RIGHT: 
                    self.turn_dir[X] -= 1
           
            

    
        # update the display
        pygame.display.update()

        return self.move_dir, self.turn_dir