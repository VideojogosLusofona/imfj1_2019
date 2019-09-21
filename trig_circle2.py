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
        draw_grid(screen, 240, 260, 50, 4, 4, 5, (255, 255, 0, 255), axis_labels_font, [str(i) for i in range(-2, 3)], [str(i) for i in range(-2, 3)])

        # Draw circle
        pygame.draw.circle(screen, (255,128, 0, 255), (340, 160), 100, 2)

        c = math.cos(math.radians(angle))
        s = math.sin(math.radians(angle))
        draw_triangle(screen, (340, 160), (340 + c * 100, 160), (340 + c * 100, 160 - s * 100), (0, 255, 0,255), 2)

        angle_start = 0
        angle_end = 0
        if (angle > 270):
            angle_start = angle
            angle_end = 360
        elif (angle > 180):
            angle_start = 180
            angle_end = angle
        elif (angle > 90):
            angle_start = angle
            angle_end = 180
        else:
            angle_start = 0
            angle_end = angle 
        pygame.draw.arc(screen, (0, 255, 255, 255), [315, 135, 50, 50], math.radians(angle_start), math.radians(angle_end), 2)

        pygame.draw.circle(screen, (255, 0, 0, 255), (int(340 + c * 100), int(160 - s * 100)), 8)
        pygame.draw.circle(screen, (255, 255, 255, 255), (int(340 + c * 100), int(160 - s * 100)), 5)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
