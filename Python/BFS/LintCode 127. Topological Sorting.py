import collections
'''
Definition for a Directed graph node
'''
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []



class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        
        
        topo = []
        inDegree = {} # 记录入度
        queue = collections.deque()
        
        # graph : 0, 1, 2, 3, 4
        # 这个模板能把整个有向图的in degree算出来
        # 当然，入度为0的点不在这个dictionary里面，因为没有人能访问到他（没有人是她的老大）
        for e in graph: # e = 0, 1, 2, 3, 4
            for i in e.neighbors: # 每个e的每个neighbor
                # 记录每个点的入度
                if i in inDegree:
                    inDegree[i] += 1 
                else:
                    inDegree[i] = 1 
        
        # 把入度为0的当作拓扑的头
        for e in graph:
            if e not in inDegree:
                queue.append(e)
        
        # bfs
        while queue:
            current = queue.popleft()
            topo.append(current)
            for e in current.neighbors:
                inDegree[e] -= 1 # 因为最前面已经pop掉了一个，那么之后的indegree都要更新
                if inDegree[e] == 0: # 把入度为0的append到队列的尾部准备遍历
                    queue.append(e)
                    
        return topo
            
            
            
        