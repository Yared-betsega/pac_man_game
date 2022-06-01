from time import sleep
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
from random import choice
from ghost import Ghost
from grids import *

class GraphicsHandler:
    def __init__(self, font) -> None:
        self.visited = set()
        self.font = font

    def playGround(self, prev, cur):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(24)
        glBegin(GL_POINTS)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    glColor3f(0.0, 0.0, 1.0)
                else:
                    glColor3f(1.0, 0.0, 0.0)
                glVertex(i, j)
        glEnd()
        glColor3f(1.0, 1.0, 0.0)
        glPointSize(5)
        glBegin(GL_POINTS)
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 0 and (i, j) not in self.visited:
                    glVertex(i, j)

        glEnd()
        self.drawHero(cur)
        self.removeEaten(prev)

    def drawHero(self, cur):
        glColor3f(1.0, 1.0, 0.0)
        glPointSize(15)
        glBegin(GL_POINTS)
        glVertex(cur[0], cur[1])
        glEnd()
    
    def removeEaten(self, prev):
        glColor3f(1.0, 0.0, 0.0)
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex(prev[0], prev[1])
        glEnd()
    
    
    def drawText(self, x, y, text):                                                
        textSurface = self.font.render(text, True, (255, 255, 66, 255), (0, 0, 0, 0))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glRasterPos2d(x, y)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

