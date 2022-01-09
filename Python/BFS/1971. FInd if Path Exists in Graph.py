from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        # create a dict to store the undirected edges for both vertices
        edge = defaultdict(set)
        for v1, v2 in edges:
            edge[v1].add(v2)
            edge[v2].add(v1)
            
        queue = [start]
        visited = set()
        
        while queue:
            currentNode = queue.pop()
            if currentNode == end:
                return True
            
            visited.add(currentNode)
            
            for vertex in edge[currentNode]:
                if vertex not in visited:
                    queue.append(vertex)
        
        return False
            
            