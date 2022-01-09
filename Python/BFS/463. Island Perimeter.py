from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # edge case
        if not grid:
            return 0
        
        m = len(grid) # num of rows
        n = len(grid[0]) # num of cols
        
        # find the first island
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    firstX = i
                    firstY = j
                    break
        grid[firstX][firstY] = 2
        
        # bfs
        queue = [(firstX, firstY)]
        perimeter = 0
        
        while queue:
            # current X and current Y
            cNode = queue.pop(0)
            cX = cNode[0]
            cY = cNode[1]
            
            cPerimeter = 4 # reset current Perimeter
            
            if cX > 0:
                if grid[cX-1][cY] != 0:
                    cPerimeter -= 1
                    if grid[cX-1][cY] == 1:
                        queue.append((cX-1, cY))
                        grid[cX-1][cY] = 2
                    
            if cY > 0:
                if grid[cX][cY-1] != 0:
                    cPerimeter -= 1
                    if grid[cX][cY-1] == 1:
                        queue.append((cX, cY-1))
                        grid[cX][cY-1] = 2
                
            if cX < m-1:
                if grid[cX+1][cY] != 0:
                    cPerimeter -= 1
                    if grid[cX+1][cY] == 1:
                        queue.append((cX+1, cY))
                        grid[cX+1][cY] = 2
                    
            if cY < n-1:
                if grid[cX][cY+1] != 0:
                    cPerimeter -= 1 
                    if grid[cX][cY+1] == 1:
                        queue.append((cX, cY+1))
                        grid[cX][cY+1] = 2
            
            perimeter += cPerimeter
            
            
        return perimeter
        