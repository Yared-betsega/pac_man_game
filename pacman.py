from random import choice
from time import sleep
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from game_controller import GameController
from ghost import Ghost 
from graphics import Acceptor, GraphicsHandler
from grids import *
from hero import Hero

global grid, difficulty
grid = choice(grids)
def init():
    pygame.init()
    display = (800,600)
    window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Pac Man Game")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-5.0, 28.0, -4.0, 20.0)
    return window

acceptor = Acceptor()
acceptor.start()
difficulty = acceptor.difficulty
init()

font = pygame.font.Font('freesansbold.ttf', 25)

def main():
    global difficulty
    graphicsHandler = GraphicsHandler(font, grid)
    gameController = GameController(grid)
    hero = Hero()
    blackGhost = Ghost(grid, (1, len(grid[0]) - 2), 0.0, 0.0, 0.0)
    greenGhost = Ghost(grid, (1, 1), 0.0, 1.0, 0.0)
    whiteGhost = Ghost(grid, (len(grid)-2, len(grid[0])-2), 1.0, 1.0, 1.0)
    tillGhost = Ghost(grid, (len(grid)-2, 1), 0.0, 1.0, 1.0)
    nowRun, lost, won = 0, False, 0
    ghostFound = []
    paused = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                print("hi")
                paused = False if paused else True
                break
            if not paused:
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
                
        if not won and not lost and not paused:
            if nowRun % 600 == 0:
                hero.timeTaken += 1

            graphicsHandler.playGround(hero)
            if nowRun % difficulty == 0:
                nextMove = gameController.nextGhostMove(blackGhost.currentPosition, (hero.x, hero.y))
                if nextMove not in ghostFound:
                    blackGhostNextMove = nextMove
                    ghostFound.append(nextMove)
                nextMove = gameController.nextGhostMove(greenGhost.currentPosition, (hero.x, hero.y))
                if nextMove not in ghostFound:
                    greenGhostNextMove = nextMove
                    ghostFound.append(nextMove)
                nextMove = gameController.nextGhostMove(whiteGhost.currentPosition, (hero.x, hero.y))
                if nextMove not in ghostFound:
                    whiteGhostNextMove = nextMove
                    ghostFound.append(nextMove)
                nextMove = gameController.nextGhostMove(tillGhost.currentPosition, (hero.x, hero.y))
                if nextMove not in ghostFound:
                    tillGhostNextMove = nextMove
                    ghostFound.append(nextMove)
            blackGhost.move(blackGhostNextMove)
            greenGhost.move(greenGhostNextMove)
            whiteGhost.move(whiteGhostNextMove)
            tillGhost.move(tillGhostNextMove)
            ghostFound.clear()
            graphicsHandler.drawText(9.5, 16, "Score: " + str(hero.score))
            graphicsHandler.drawText(7, 18, "Target Score: " + str(gameController.targetScore))
            graphicsHandler.drawText(0., 18, "Time: " + str(hero.timeTaken))

        pygame.display.flip()

        won = won or gameController.checkWin(hero.score)
        if won:
            graphicsHandler.displayWinScreen(hero.score, hero.timeTaken)
        if not won:
            lost = lost or gameController.checkLoss(blackGhost.currentPosition, (hero.x, hero.y))
            lost = lost or gameController.checkLoss(greenGhost.currentPosition, (hero.x, hero.y))
            lost = lost or gameController.checkLoss(whiteGhost.currentPosition, (hero.x, hero.y))
            lost = lost or gameController.checkLoss(tillGhost.currentPosition, (hero.x, hero.y))
        if lost:
            graphicsHandler.displayLossScreen((hero.x, hero.y), hero.score, hero.timeTaken)

        pygame.time.wait(10)
        nowRun += 10
        

main()