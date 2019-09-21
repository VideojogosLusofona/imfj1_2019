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

    coord = 0

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                exit()
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    coord = coord - 0.25
                    if (coord < 0):
                        coord = 0
                elif (event.key == pygame.K_RIGHT):
                    coord = coord + 0.25
                    if (coord > 14):
                        coord = 14


        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,20))
       
        # Draw axis
        draw_graph_axis_x(screen, 40, 240, 40, 14, 5, (255, 255, 0, 255), axis_labels_font, [ str(i) for i in range(0, 15) ])

        # Draw character
        draw_character(screen, 40 + coord * 40, 220, 40, 120, (255, 128, 0, 255), 2, 0)

        # Write coordinate
        axis_labels_font.render_to(screen, (4 + coord * 40, 80), "Coordinates = (" + str(coord) + ")", (0, 255, 0))

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
