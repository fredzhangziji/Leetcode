class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        
        #注意这里的范围是1~max(L)，因为最短的那根可能用不上。
        startL = 1
        endL = max(L)
        
        while startL + 1 < endL:
            midL = (startL + endL) // 2
            if self.findK(L, midL) >= k:
                startL = midL
            else:
                endL = midL
        
        
        if self.findK(L, endL) >= k:
            return endL
        elif self.findK(L, startL) >= k:
            return startL
        else:
            return 0
            
    
    def findK(self, L, length):
        res = 0
        for log in L:
            res += log // length
        
        return res
                