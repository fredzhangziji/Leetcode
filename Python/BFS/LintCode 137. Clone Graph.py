import collections

class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        
        if not node:
            return node

        queue = collections.deque([node])
        visited = {node: UndirectedGraphNode(node.label)}
        
        while queue:
            currNode = queue.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = UndirectedGraphNode(neighbor.label)
                visited[currNode].neighbors.append(visited[neighbor])
                        
        return visited[node]