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

def lerp(p1, p2, t, func = None):
    tt = t
    if (func != None):
        tt = func(t)

    return p1[0] + tt * (p2[0] - p1[0]), p1[1] + tt * (p2[1] - p1[1])    

def ease_function(t):
    return t

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

    t = 0
    t_inc = 0.0025

    # Game loop, runs forever
    while (True):   
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                exit()
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_DOWN):
                    t_inc *= 0.9
                if (event.key == pygame.K_UP):
                    t_inc *= 1.1

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,20))
       
        # Draw grid
        draw_grid(screen, grid_base[0], grid_base[1], grid_divs, 6, 6, 5, (64, 64, 0, 255), axis_labels_font, [str(i) for i in range(-3, 4)], [str(i) for i in range(-3, 4)])

        p = lerp((0, 0), (2, 0), t, ease_function)
        p = convert_coord(p[0], p[1])

        draw_character(screen, p[0], p[1], 40, 80, (255, 255, 0, 255), 2, 0)

        axis_labels_font.render_to(screen, (20, 20), "T = " + str(t), (0, 255, 0))

        t = t + t_inc
        if (t >= 1):
            t = 1
            t_inc = -t_inc
        elif (t <= 0):
            t = 0
            t_inc = -t_inc

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
