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

# Define a main function, just to keep things nice and tidy
def main():
    global grid_base
    global grid_divs

    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res = (640, 640)
    # Create a window and a display surface
    screen = pygame.display.set_mode(res)

    # Load a font
    axis_labels_font = pygame.freetype.Font("NotoSans-Regular.ttf", 12)
    vector_labels_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

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
        draw_grid(screen, grid_base[0], grid_base[1], grid_divs, 6, 6, 5, (64, 64, 0, 255), axis_labels_font, [str(i) for i in range(-3, 4)], [str(i) for i in range(-3, 4)])

        draw_vector(screen, (0, 255, 0, 255), convert_coord(0,0), convert_coord(2,-1), 2, vector_labels_font, "a", -12)
        draw_vector(screen, (255, 0, 0, 255), convert_coord(0,0), convert_coord(2,0), 2, vector_labels_font, "v", -12)
        draw_vector(screen, (0, 255, 255, 255), convert_coord(0,0), convert_coord(2,1), 2, vector_labels_font, "b", 24)

        x,y = convert_coord(0,0)
        
        pygame.draw.arc(screen, (255, 0, 255, 255), [x-50, y - 50, 100, 100], math.radians(-30), math.radians(30), 2)
        
        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


# Run the main function
main()
