# Import pygame into our program
import pygame
import pygame.freetype
import math
import time

from helpers import * 

# Define a main function, just to keep things nice and tidy
def main():

    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res = (640, 360)
    # Create a window and a display surface
    screen = pygame.display.set_mode(res)

    # Load a font
    axis_labels_font = pygame.freetype.Font("NotoSans-Regular.ttf", 12)

    angle = 30

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
        draw_grid(screen, 240, 260, 100, 2, 2, 5, (255, 255, 0, 255), axis_labels_font, [str(i) for i in range(-1, 2)], [str(i) for i in range(-1, 2)])

        # Draw circle
        pygame.draw.circle(screen, (255,128, 0, 255), (340, 160), 100, 2)

        angle = 30
        c = math.cos(math.radians(angle))
        s = math.sin(math.radians(angle))
        draw_triangle(screen, (340, 160), (340 + c * 100, 160), (340 + c * 100, 160 - s * 100), (0, 255, 0,255), 2)
        pygame.draw.arc(screen, (0, 255, 255, 255), [315, 135, 50, 50], math.radians(0), math.radians(angle), 2)

        angle = 150
        c = math.cos(math.radians(angle))
        s = math.sin(math.radians(angle))
        draw_triangle(screen, (340, 160), (340 + c * 100, 160), (340 + c * 100, 160 - s * 100), (0, 255, 0,255), 2)
        pygame.draw.arc(screen, (0, 255, 255, 255), [315, 135, 50, 50], math.radians(angle), math.radians(180), 2)


        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
