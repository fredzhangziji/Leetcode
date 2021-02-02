"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
DIRECTION = [
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1)
]

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        
        if not grid or not grid[0]:
            return -1
        
        queue = collections.deque([source])
        pathLength = 0
        
        while queue:
            for _ in range(len(queue)):
                # 这段代码会超过memory limit
                # currPos = queue.popleft()
                # if currPos.x == destination.x and currPos.y == destination.y:
                #     return pathLength
                # grid[currPos.x][currPos.y] == "Visited"
                # for deltaX, deltaY in DIRECTION:
                #     newX, newY = currPos.x + deltaX, currPos.y + deltaY
                #     if self.isValid(newX, newY, grid):
                #         queue.append(Point(newX, newY))
                
                if queue[0].x == destination.x and queue[0].y == destination.y:
                    return pathLength
                
                for deltaX, deltaY in DIRECTION:
                    newX, newY = queue[0].x + deltaX, queue[0].y + deltaY
                    if self.isValid(newX, newY, grid):
                        queue.append(Point(newX, newY))
                        grid[newX][newY] = "Visited"
                        
                queue.popleft()
                
            pathLength += 1 
        
        return -1
        
    def isValid(self, x, y, grid):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False 
        if grid[x][y] == "Visited":
            return False
        if grid[x][y] == 1:
            return False
        
        return True
        