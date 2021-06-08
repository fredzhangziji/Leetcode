class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)
        
        for source in graph:
            graph[source].sort(reverse = True)
        
        res = []
        stack = ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                res.append(stack.pop())
            
        return res[::-1]