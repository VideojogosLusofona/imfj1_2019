# Import pygame into our program
import pygame
import pygame.freetype

from helpers import * 

grid_base = (80, 560)
grid_divs = 80
grid_center = (320, 320)

def convert_coord(x,y):
    global grid_center
    global grid_divs

    return (grid_center[0] + x * grid_divs, grid_center[1] - y * grid_divs)

def draw_function(screen, color, func, domain = None):
    if (domain == None):
        x = prev_x = -3
        prev_y = func(prev_x)
    else:
        x = prev_x = domain[0]
        prev_y = func(prev_x)
    while (x < 3):
        x = x + 0.025
        if (domain != None):
            if ((x < domain[0]) or (x > domain[1])):
                continue
        pygame.draw.aaline(screen, color, convert_coord(prev_x, prev_y), convert_coord(x, func(x)))
        prev_x = x
        prev_y = func(x)

def draw_function_y(screen, color, func, domain = None):
    if (domain == None):
        y = prev_y = -3
        prev_x = func(prev_y)
    else:
        y = prev_y = domain[0]
        prev_x = func(prev_y)
    while (y < 3):
        y = y + 0.025
        if (domain != None):
            if ((y < domain[0]) or (y > domain[1])):
                continue
        pygame.draw.aaline(screen, color, convert_coord(prev_x, prev_y), convert_coord(func(y), y))
        prev_y = y
        prev_x = func(y)

# Define a main function, just to keep things nice and tidy
def main():

    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res = (640, 640)
    # Create a window and a display surface
    screen = pygame.display.set_mode(res)

    # Load a font
    axis_labels_font = pygame.freetype.Font("NotoSans-Regular.ttf", 12)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                exit()

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,20))
       
        # Draw grid
        draw_grid(screen, grid_base[0], grid_base[1], grid_divs, 6, 6, 5, (64, 128, 64, 255), axis_labels_font, [str(i) for i in range(-3, 4)], [str(i) for i in range(-3, 4)])

        draw_function_y(screen, (255, 255, 0, 255), lambda x : 2)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
