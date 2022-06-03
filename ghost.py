from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
from random import choice

class Ghost:
    def __init__(self, grid, initialpos, r, g, b) -> None:
        self.currentPosition = initialpos
        self.color = (r, g, b)
        glColor3f(r, g, b)
        glPointSize(15)
        glBegin(GL_POINTS)
        glVertex(len(grid)//2, len(grid[0])//2)
        glEnd()

    def move(self, coordinate):
        self.currentPosition = coordinate
        glColor3f(self.color[0], self.color[1], self.color[2])
        glPointSize(15)
        glBegin(GL_POINTS)
        glVertex(coordinate[0], coordinate[1])
        glEnd()

    