import pygame
import math

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

def get_dir(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    n = math.sqrt(dx*dx + dy*dy)

    return (dx / n, dy / n), n

def draw_vector(screen, color, p1, p2, width, font = None, name = "", offset = 10):
    pygame.draw.line(screen, color, p1, p2, width)

    dir, length = get_dir(p1, p2)
    perp = (-dir[1], dir[0])

    p3 = (p2[0] - dir[0] * 10 + perp[0] * 10, p2[1] - dir[1] * 10 + perp[1] * 10)
    p4 = (p2[0] - dir[0] * 10 - perp[0] * 10, p2[1] - dir[1] * 10 - perp[1] * 10)

    pygame.draw.line(screen, color, p2, p3, width)
    pygame.draw.line(screen, color, p2, p4, width)

    if (font != None):
        c = (p1[0] + dir[0] * length * 0.5 - perp[0] * offset, p1[1] + dir[1] * length * 0.5 - perp[1] * offset)
        font.render_to(screen, c, name, color)

def draw_dashed_line(screen, color, p1, p2, width, n_dash, font = None, name ="", offset = 10):
    dir, length = get_dir(p1, p2)
    p = p1

    l = 0.5 * length / n_dash

    for i in range(0, n_dash):
        pygame.draw.line(screen, color, p, (p[0] + dir[0] * l, p[1] + dir[1] * l), width)
        p = (p[0] + dir[0] * l * 2, p[1] + dir[1] * l * 2)

    if (font != None):
        c = (p1[0] + dir[0] * length * 0.5, p1[1] + dir[1] * length * 0.5 - offset)
        font.render_to(screen, c, name, color)

def draw_label(screen, color, p, font, name):
    if (font != None):
        font.render_to(screen, p, name, color)

def draw_point(screen, color, p, size, font = None, name = "", offset = 10):
    pygame.draw.circle(screen, color, p, size)
    if (font != None):
        draw_label(screen, color, (p[0] + offset, p[1]), font, name)
