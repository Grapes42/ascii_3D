import pygame

class GUIInterface():
    def __init__(self, chars_height, chars_width, pixel_height, pixel_width, frame_rate=20, font="Monospace", font_size=5, line_spacing=1, fg_color=(255,255,255), bg_color=(0,0,0)) -> None:
        self.clock = pygame.time.Clock()
        self.frame_rate = frame_rate
        
        self.chars_height = chars_height
        self.chars_width = chars_width

        self.font = font
        self.font_size = font_size

        self.fg_color = fg_color
        self.bg_color = bg_color

        pygame.font.init()
 
        pygame.font.get_init()
        
        self.display_surface = pygame.display.set_mode((pixel_width, pixel_height))
        
        pygame.display.set_caption('Our Text')

        self.font = pygame.font.SysFont(font, font_size)

        self.rendered_rows = []

        for y in range(self.chars_height):
            self.rendered_rows.append(self.font.render("#"*chars_width, True, self.fg_color))

        self.rectangles = []

        y_pos = 0

        for y in range(self.chars_height):
            self.rectangles.append(self.rendered_rows[y].get_rect())

            self.rectangles[y].center = (round(pixel_width/2),y_pos)

            y_pos += line_spacing



    def update(self, array):
        #"""
        str_rows = []

        for y in range(len(array)):
            line = ""
            for x in range(len(array[0])):
                line += str(array[y, x])
            str_rows.append(line)

        for y in range(self.chars_height):
            self.rendered_rows[y] = self.font.render(str_rows[y], True, self.fg_color)
        #"""

        self.display_surface.fill(self.bg_color)

        for y in range(self.chars_height):
            self.display_surface.blit(self.rendered_rows[y], self.rectangles[y])

        for event in pygame.event.get():
 
            if event.type == pygame.QUIT:
            
                # deactivating the pygame library
                pygame.quit()
    
                # quitting the program.
                quit()
    
            # update the display
        pygame.display.update()

        self.clock.tick(self.frame_rate)