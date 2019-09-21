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

    x,y = 2, 2

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
                    x = x - 0.25
                    if (x < -7):
                        x = -7
                elif (event.key == pygame.K_RIGHT):
                    x = x + 0.25
                    if (x > 7):
                        x = 7
                elif (event.key == pygame.K_DOWN):
                    y = y - 0.25
                    if (y < 0):
                        y = 0
                elif (event.key == pygame.K_UP):
                    y = y + 0.25
                    if (y > 6):
                        y = 6

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,20))
       
        # Draw grid
        draw_grid(screen, 40, 320, 40, 14, 7, 5, (255, 255, 0, 255), axis_labels_font)

        # Draw character
        screen_x = 40 + x * 40
        screen_y = 320 - y * 40

        draw_character(screen, screen_x, screen_y, 20, 60, (255, 128, 0, 255), 2, 2)

        # Write coordinate
        axis_labels_font.render_to(screen, (screen_x + 10, screen_y - 70), "Coordinates = (" + str(x) + "," + str(y) + ")", (0, 255, 0))

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
