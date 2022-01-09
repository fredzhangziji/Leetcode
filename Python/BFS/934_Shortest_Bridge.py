import collections
from typing import List
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # 这一题的思路就是dfs+bfs
        # 用dfs来找其中一个岛的所有点，然后把这些点都push到queue里面
        # 然后用bfs来遍历这个queue
        # 当遍历到第二个岛的时候，最短路径就被找到了
        
        queue = collections.deque()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        # 遍历A来找第一个1，然后开始dfs来找所有岛上的点
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    self.dfs(A, i, j, queue)
                    break
            if A[i][j] == 2:
                break
                
                
        # 这个时候第一个岛的所有点已经被加到queue里了
        step = 0
        while queue:
            size = len(queue)
            for s in range(size):   # bfs经典模版来记录层数
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx = x+dx
                    ny = y+dy
                    if 0<=nx<len(A) and 0<=ny<len(A[0]):
                        if A[nx][ny] == 1:  # 表示第二个岛找到了（因为第一个岛全部是2了）
                            return step
                        if A[nx][ny] == 0:
                            A[nx][ny] = 2  # 说明没找到，那直接标记成2，继续找
                            queue.append((nx,ny))
            step += 1
        
        
        
    def dfs(self, A,x,y,queue):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        if 0<=x<len(A) and 0<=y<len(A[0]) and A[x][y] == 1:
            A[x][y] = 2
            queue.append((x,y))
            for i,j in directions:
                self.dfs(A,x+i,y+j,queue)
        else:
            return
        
                    
        

                
            
        
        