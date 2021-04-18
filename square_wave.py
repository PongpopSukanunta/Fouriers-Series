"""
aniamated fourier series using circles
"""

import os
import sys
import math
import pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'

# pygame setup
pygame.init()
pygame.display.set_caption("Fourier's Series")
width, height = 1000, 600
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

# color
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)
green = (100, 149, 104)

#constant
wave_start_x = 400
circle_center_x = 150
circle_center_y = 300
num = 10

# variables
angle = 0
dot_y = 0
wave = []

def draw_circles(start_x, start_y, circle_num, start_size):
    global dot_y
    center_x = start_x
    center_y = start_y
    for n in range(circle_num):
        i = 2 * n + 1
        radius = start_size * 4 / (i * math.pi)
        x = center_x + radius * math.cos(i * angle)
        y = center_y + radius * math.sin(i * angle)
        pygame.draw.circle(screen, white, (center_x, center_y), radius, 2)
        pygame.draw.line(screen, gray, (center_x, center_y), (x, y))
        # set next circle center to be on the circumference of the previous
        center_x = x
        center_y = y
        dot_y = y
        # draw a line from last circle
        if n == circle_num - 1:
            pygame.draw.line(screen, gray, (center_x, center_y), (wave_start_x, y))
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break

    # set pygame
    clock.tick(fps)
    screen.fill(black)

    draw_circles(circle_center_x, circle_center_y, num, 60)

    new_dot = [wave_start_x, dot_y]
    wave.insert(0, new_dot)
    # move all the dots to the right and draw them
    for dot in wave:
        dot[0] += 3 # x += 3
        pygame.draw.circle(screen, white, (dot[0], dot[1]), 3)

    # remove dot if exceed 200 dots
    if len(wave) > 300:
        wave.pop()


    angle -= 0.05

    pygame.display.flip()