from time import sleep
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


class GraphicsHandler:
    def __init__(self, font, grid) -> None:
        self.font = font
        self.grid = grid 

    def playGround(self, hero):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(24)
        glBegin(GL_POINTS)

        # Draw the Grid using the red and blue points
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    glColor3f(0.0, 0.0, 1.0)
                else:
                    glColor3f(1.0, 0.0, 0.0)
                glVertex(i, j)
        glEnd()

        # Draw the yellow Dots (Foods)
        glColor3f(1.0, 1.0, 0.0)
        glPointSize(5)
        glBegin(GL_POINTS)
        for i in range(1, len(self.grid)-1):
            for j in range(1, len(self.grid[0])-1):
                if self.grid[i][j] == 0 and (i, j) not in hero.visited:
                    glVertex(i, j)
        glEnd()

        # Draw the hero and remove the eaten fruit
        self.drawHero(hero)

        self.drawText(-0, -3, "Press Space to pause", (255, 255, 255, 255))
        self.drawText(13, -3, "Press Enter to restart", (255, 255, 255, 255))

    def drawHero(self, hero):
        glColor3f(1.0, 1.0, 0.0)
        glPointSize(15)
        glBegin(GL_POINTS)
        glVertex(hero.x,hero.y)
        glEnd()
     
    def drawText(self, x, y, text, color = (255, 255, 66, 255)):                                                
        textSurface = self.font.render(text, True, color, (0, 0, 0, 0))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glRasterPos2d(x, y)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

    def displayWinScreen(self, score, timeTaken):
        glClear(GL_COLOR_BUFFER_BIT)
        self.drawText(9.5, 9, "You Won!!")
        self.drawText(8, 7, "Your Score: " + str(score))
        minutes = timeTaken // 60
        seconds = timeTaken % 60
        self.drawText(8.5, 5, "Your time: 0" + str(minutes) + " : " + str(seconds))
        self.drawText(7, 2, "Press Enter to restart", (255, 255, 255, 255))
        
        pygame.display.flip()
    
    def displayLossScreen(self, player, score, timeTaken):
        
        pygame.display.flip()
        glClear(GL_COLOR_BUFFER_BIT)
        self.drawText(9.5, 9, "You Lost!!")
        self.drawText(8, 7, "Your Score: " + str(score))
        minutes = timeTaken // 60
        seconds = timeTaken % 60
        self.drawText(8.5, 5, "Your time: 0" + str(minutes) + " : " + str(seconds))
        self.drawText(7, 2, "Press Enter to restart", (255, 255, 255, 255))
        
        pygame.display.flip()

# Accept The Functions
import tkinter as tk
class Acceptor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PacMan Game")
        self.title = tk.Label(self.root, text="Choose Difficulty",height=3, width=40, font=("Helvetica 15 bold"), bg="black", fg="white")
        self.easy = tk.Button(self.root, text="Easy",width=10, height=2, cursor="hand2", font=12, fg="black", bg="yellow", borderwidth=2, padx=10, pady=5,command=lambda:self.chooseDifficulty("easy"))
        self.medium = tk.Button(self.root, text="Medium",width=10, height=2, cursor="hand2", font=12, fg="black", bg="lightgreen", borderwidth=2, padx=10, pady=5,command=lambda:self.chooseDifficulty("medium"))
        self.hard = tk.Button(self.root, text="Hard",width=10, height=2, cursor="hand2", font=12, fg="black", bg="mediumblue", borderwidth=2, padx=10, pady=5,command=lambda:self.chooseDifficulty("hard"))
        self.hell = tk.Button(self.root, text="Hell",width=10, height=2, cursor="hand2", font=12, fg="black", bg="darkred", borderwidth=2, padx=10, pady=5,command=lambda:self.chooseDifficulty("hell"))
        self.difficulty = None

    def start(self):
        self.title.grid(row = 0, column=0, columnspan=2)
        self.easy.grid(row=1, column=0, pady=10, columnspan=2)
        self.medium.grid(row=2, column=0, pady=10, columnspan=2)
        self.hard.grid(row=3, column=0, pady=10, columnspan=2)
        self.hell.grid(row=4, column=0, pady=10, columnspan=2)
        self.root.mainloop()
    
    def chooseDifficulty(self, diff):
        if diff == "easy":
            self.difficulty = 500
        elif diff == "medium":
            self.difficulty = 400
        elif diff == "hard":
            self.difficulty = 300
        else:
            self.difficulty = 200
        self.root.destroy()


