from collections import deque

class GameEngine:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.isValidMove = lambda point: 0 <= point[0] < len(grid)-1 and 0 <= point[1] < len(grid[0])-1 and grid[point[0]][point[1]] == 0
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(self, source, destination):
        visited = set()
        queue = deque([(source, [])])

        while queue:
            cur, path = queue.popleft()
            path.append(cur)
            if cur == destination:
                return path[1]
            for neighbor in self.directions:
                nextMove = (cur[0]+neighbor[0], cur[1]+neighbor[1])
                if self.isValidMove(nextMove) and nextMove not in visited:
                    queue.append((nextMove, path+[nextMove]))
                    visited.add(nextMove)
    
    