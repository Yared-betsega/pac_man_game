from random import choice
from grids import *

class GameController:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.isValidMove = lambda point: 0 <= point[0] < len(grid)-1 and 0 <= point[1] < len(grid[0])-1 and grid[point[0]][point[1]] == 0
        self.targetScore = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.targetScore += 1

    def nextGhostMove(self, current):
        while True:
            direction = choice(self.directions)
            next = (current[0] + direction[0], current[1] + direction[1])
            if self.isValidMove(next):
                return next
    
    def checkLoss(self, ghost, player):
        if ghost == player:
            return True
        return False

    def checkWin(self, score):
        if score == self.targetScore:
            return True
        return False     
