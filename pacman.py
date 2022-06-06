from random import choice
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from game_controller import GameController
from ghost import Ghost
from graphics import GraphicsHandler
from grids import *
from hero import Hero

global grid
grid = choice(grids)
def init():
    pygame.init()
    display = (800,600)
    window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Pac Man Game")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-5.0, 28.0, -4.0, 20.0)
    return window


init()

font = pygame.font.Font('freesansbold.ttf', 25)

def main():
    graphicsHandler = GraphicsHandler(font, grid)
    gameController = GameController(grid)
    hero = Hero()
    blackGhost = Ghost(grid, (1, len(grid[0]) - 2), 0.0, 0.0, 0.0)
    greenGhost = Ghost(grid, (1, 1), 0.0, 1.0, 0.0)
    whiteGhost = Ghost(grid, (len(grid)-2, len(grid[0])-2), 1.0, 1.0, 1.0)
    tillGhost = Ghost(grid, (len(grid)-2, 1), 0.0, 1.0, 1.0)
    nowRun, lost, won = 0, False, 0
