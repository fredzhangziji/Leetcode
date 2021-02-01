import collections
class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here

        numPpl = len(M)
        ans = 0
        visited = {}
        for i in range(numPpl):
            visited[i] = False
        
        for i in range(numPpl):
            if visited[i] == False:
                # bfs
                ans += 1 
                visited[i] = True
                queue = collections.deque([i])
                while queue:
                    currPerson = queue.popleft()
                    for j in range(numPpl):
                        if M[currPerson][j] == 1 and visited[j] == False:
                            visited[j] = True
                            queue.append(j)
        
        return ans
        