# Import pygame into our program
import pygame
import pygame.freetype

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
       
        draw_grid(screen, 80, 280, 40, 12, 6, 5, (0, 255, 255, 255), axis_labels_font)

        pygame.draw.line(screen, (255, 255, 0, 255), (80, 280), (560, 280), 2)
        pygame.draw.line(screen, (255, 255, 0, 255), (560, 280), (560, 80), 2)
        pygame.draw.line(screen, (255, 255, 0, 255), (80, 280), (560, 80), 2)


        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
