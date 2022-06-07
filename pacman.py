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
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if hero.x > 1 and grid[hero.x-1][hero.y] != 1:
                    hero.moveLeft()
                    
            if keys[pygame.K_RIGHT]:
                if hero.x < 29 and grid[hero.x+1][hero.y] != 1:
                    hero.moveRight()
                    
            if keys[pygame.K_UP]:
                if hero.y < 16 and grid[hero.x][hero.y+1] != 1:
                    hero.moveUp()
                    
            if keys[pygame.K_DOWN]:
                if hero.y > 1 and grid[hero.x][hero.y-1] != 1:
                    hero.moveDown()

        if not won and not lost:
            graphicsHandler.playGround(hero)
            if nowRun % 200 == 0:
                blackGhostNextMove = gameController.nextGhostMove(blackGhost.currentPosition)
                greenGhostNextMove = gameController. nextGhostMove(greenGhost.currentPosition)
                whiteGhostNextMove = gameController.nextGhostMove(whiteGhost.currentPosition)
