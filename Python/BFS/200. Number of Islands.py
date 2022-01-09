from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case
        if not grid:
            return 0
        
        # bfs queue & island count
        queue = []
        count = 0
        
        # num of rows, num of cols
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    queue.append((i, j))
                    grid[i][j] = "2" # mark the point as "visited"
                    
                    # iterate thru the queue till the queue is empty
                    # which means that we explore the whole island
                    while queue:
                        x, y = queue[0][0], queue[0][1]
                        
                        # border check & island check
                        if x - 1 >= 0:
                            if grid[x-1][y] == "1":
                                queue.append((x-1, y))
                                grid[x-1][y] = "2" # mark the point as "visited"
                        if x + 1 <= m - 1:
                            if grid[x+1][y] == "1":
                                queue.append((x+1, y))
                                grid[x+1][y] = "2" # mark the point as "visited"
                        if y - 1 >= 0:
                            if grid[x][y-1] == "1":
                                queue.append((x, y-1))
                                grid[x][y-1] = "2" # mark the point as "visited"
                        if y + 1 <= n - 1:
                            if grid[x][y+1] == "1":
                                queue.append((x, y+1))
                                grid[x][y+1] = "2" # mark the point as "visited"
                        
                        queue.pop(0) # get rid of this obselete point
                    
                    count += 1 # increment the number of island
        
        return count