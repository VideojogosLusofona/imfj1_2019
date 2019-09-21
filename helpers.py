import pygame

def draw_graph_axis_x(screen, x, y, x_inc, x_count, div_size, color, font = None, values = None):
    current_x = x
    for i in range(0, x_count + 1):
        pygame.draw.aaline(screen, color, (current_x, y - div_size), (current_x, y + div_size))

        if (font != None):
            width = font.get_rect(values[i]).width
            font.render_to(screen, (current_x - width * 0.5, y + div_size + 4), values[i], color)

        current_x = current_x + x_inc

    pygame.draw.aaline(screen, color, (x,y), (x + x_count * x_inc, y))
    
def draw_graph_axis_y(screen, x, y, y_inc, y_count, div_size, color, font = None, values = None):
    current_y = y
    for i in range(0, y_count + 1):
        pygame.draw.aaline(screen, color, (x - div_size, current_y), (x + div_size, current_y))

        if (font != None):
            height = font.get_rect(values[i]).height
            font.render_to(screen, (x - div_size - 10, current_y - height * 0.5), values[i], color)

        current_y = current_y - y_inc

    pygame.draw.aaline(screen, color, (x,y), (x, y - y_count * y_inc))
    
def draw_character(screen, x, y, width, height, color, line_width, pivot_width):
    pygame.draw.line(screen, color, (x - width * 0.5, y), (x, y - height * 0.3), line_width)
    pygame.draw.line(screen, color, (x + width * 0.5, y), (x, y - height * 0.3), line_width)
    pygame.draw.line(screen, color, (x, y - height * 0.3), (x, y - height * 0.7), line_width)
    pygame.draw.line(screen, color, (x, y - height * 0.6), (x + width * 0.5, y - height * 0.4), line_width)
    pygame.draw.line(screen, color, (x, y - height * 0.6), (x - width * 0.5, y - height * 0.4), line_width)
    pygame.draw.circle(screen, color, (int(x), int(y - height * 0.85)), int(height * 0.15), line_width)

    if (pivot_width > 0):
        pygame.draw.circle(screen, color, (int(x),int(y)), pivot_width)

def draw_grid(screen, x, y, grid_division, x_count, y_count, div_size, color, font, labels_x = None, labels_y = None):
    for yy in range(0, y_count + 1):
        pygame.draw.aaline(screen, color, (x, y - yy * grid_division), (x + x_count * grid_division, y - yy * grid_division))
    for xx in range(0, x_count + 1):
        pygame.draw.aaline(screen, color, (x + xx * grid_division, y), (x + xx * grid_division, y - y_count * grid_division))

    lx = [str(i) for i in range(0, x_count + 1)]
    if (labels_x != None):
        lx = labels_x
    ly = [str(i) for i in range(0, y_count + 1)]
    if (labels_y != None):
        ly = labels_y

    draw_graph_axis_x(screen, x, y, grid_division, x_count, div_size, color, font, lx)
    draw_graph_axis_y(screen, x, y, grid_division, y_count, div_size, color, font, ly)

def draw_triangle(screen, p1, p2, p3, color, width):
    pygame.draw.line(screen, color, p1, p2, width)
    pygame.draw.line(screen, color, p2, p3, width)
    pygame.draw.line(screen, color, p3, p1, width)