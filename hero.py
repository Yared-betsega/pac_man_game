from grids import *

class Hero :
    def __init__(self) -> None:
        self.x = 12
        self.y = 1
        self.score = 1
        self.timeTaken = 0
        self.visited = set([(self.x, self.y)])

    def moveLeft(self):
        self.x-=1
        if (self.x, self.y) not in self.visited:
            self.score += 1
            self.visited.add((self.x, self.y))

    def moveRight(self):
        self.x += 1
        if (self.x, self.y) not in self.visited:
            self.score += 1
            self.visited.add((self.x, self.y))

    def moveUp(self):
        self.y += 1
        if (self.x, self.y) not in self.visited:
            self.score += 1
            self.visited.add((self.x, self.y))

    def moveDown(self):
        self.y -= 1
        if (self.x, self.y) not in self.visited:
            self.score += 1
            self.visited.add((self.x, self.y))


                    