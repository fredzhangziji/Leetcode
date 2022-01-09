import collections

DIRECTION = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
    ]

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        
        if not grid or not grid[0]:
            return 0
        
        visited = set()
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    ans += 1 
        
        return ans
    
    def bfs(self, grid, i, j, visited):
        visited.add((i, j))
        queue = collections.deque([(i, j)])
        while queue:
            currentX, currentY = queue.popleft()
            for nextX, nextY in DIRECTION:
                newX, newY = currentX + nextX, currentY + nextY
                if self.isValid(newX, newY, grid, visited):
                    queue.append((newX, newY))
                    visited.add((newX, newY))
                    
    def isValid(self, i, j, grid, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return False
        if (i, j) in visited:
            return False
        if grid[i][j] == 0:
            return False
        
        return True
        
        