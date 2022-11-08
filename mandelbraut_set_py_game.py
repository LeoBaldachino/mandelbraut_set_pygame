import pygame as pg
import numpy as np
import time
import sys
import os
import math
import random
import time
import datetime
# i import bunch of stuff here

# The goal of this program is to create a mandelbrot set using pygame and numpy to showoff the power of numpy and to get verified on HiddenDevs discord server
# This is Leoleo hello yes

# initialize pygame
pg.init()
pg.font.init()
pg.display.init()
pg.display.set_caption("Mandelbrot Set")

# set up the window
screen = pg.display.set_mode((800, 600))
screen.fill((0, 0, 0))
pg.display.flip()

# set up the fonts
font = pg.font.SysFont('Arial', 20)

# set up some helper functions
def map_range(value, low1, high1, low2, high2):
    return low2 + (high2 - low2) * (value - low1) / (high1 - low1)
    # helper function to map a value from one range to another



# set up the variables
x = 0
y = 0
w = 800
h = 600
maxiterations = 50
zoom = 1
moveX = 0
moveY = 0
zoom = 1
zoomSpeed = 1.1
moveSpeed = 0.01
zoomIn = False
zoomOut = False
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
running = True
start_time = time.time()
fps = 0

# Setup a clock for a decent framerate and a timer for the fps counter
clock = pg.time.Clock()
timer = time.time()

# main loop
while running:
    # check for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_UP:
                moveUp = True
            if event.key == pg.K_DOWN:
                moveDown = True
            if event.key == pg.K_LEFT:
                moveLeft = True
            if event.key == pg.K_RIGHT:
                moveRight = True
            if event.key == pg.K_EQUALS:
                zoomIn = True
            if event.key == pg.K_MINUS:
                zoomOut = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                moveUp = False
            if event.key == pg.K_DOWN:
                moveDown = False
            if event.key == pg.K_LEFT:
                moveLeft = False
            if event.key == pg.K_RIGHT:
                moveRight = False
            if event.key == pg.K_EQUALS:
                zoomIn = False
            if event.key == pg.K_MINUS:
                zoomOut = False

    # handle movement and zooming
    if moveUp:
        moveY -= moveSpeed
    if moveDown:
        moveY += moveSpeed
    if moveLeft:
        moveX -= moveSpeed
    if moveRight:
        moveX += moveSpeed
    if zoomIn:
        zoom *= zoomSpeed
    if zoomOut:
        zoom /= zoomSpeed

    # create a numpy array of complex numbers
    c = np.zeros((w, h), dtype=np.complex64)
    for i in range(w):
        for j in range(h):
            c[i, j] = complex(map_range(i, 0, w, -2, 2) / zoom + moveX, map_range(j, 0, h, -1, 1) / zoom + moveY)

    # create a numpy array of iterations
    iterations = np.zeros((w, h), dtype=np.int32)

    # create a numpy array of booleans
    z = np.zeros((w, h), dtype=np.bool)

    # create a numpy array of colors
    colors = np.zeros((w, h), dtype=np.uint32)

    # create a numpy array of the mandelbrot set
    mandelbrot = np.zeros((w, h), dtype=np.uint32)

    # display the mandelbrot set
    for i in range(maxiterations):
        z = z * z + c
        iterations[np.logical_and(z, iterations == i)] = i + 1 # this is the line that makes it so fast

    # create the colors
    colors = np.uint32(np.arctan2(np.imag(z), np.real(z)) * 255 / (2 * np.pi))
    colors[np.logical_not(z)] = 0

    # create the mandelbrot set
    mandelbrot = np.uint32(np.arctan2(np.imag(z), np.real(z)) * 255 / (2 * np.pi))
    mandelbrot[np.logical_not(z)] = 0

    # create the surface
    surface = pg.surfarray.make_surface(mandelbrot)

    # blit the surface to the screen
    screen.blit(surface, (0, 0))

    # update the display
    pg.display.flip()

    # update the clock
    clock.tick(60)

    # update the fps counter
    fps += 1
    if time.time() - timer > 1:
        timer = time.time()
        print(fps)
        fps = 0

# quit pygame
pg.quit()

# quit python
sys.exit()