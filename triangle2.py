# Import pygame into our program
import pygame
import pygame.freetype
import math

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

        x = 80
        y = 280
        width = 480
        height = 200
       
        pygame.draw.line(screen, (255, 255, 0, 255), (x, y), (x + width, y), 2)
        pygame.draw.line(screen, (255, 255, 0, 255), (x + width, y), (x + width, y - height), 2)
        pygame.draw.line(screen, (255, 255, 0, 255), (x + width, y - height), (x, y), 2)
        
        pygame.draw.arc(screen, (0, 255, 255, 255), [-20, 180, 200, 200], math.radians(0), math.asin(height/width), 2)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
