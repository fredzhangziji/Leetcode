class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here

        pos = 0
        neg = 0
        
        for num in A:
            if num > 0:
                pos += 1 
            elif num < 0: 
                neg += 1 
        
        self.partition(A, pos > neg)
        self.interleaving(A, pos == neg)
    
    def partition(self, A, startIsPos):
        flag = 1 if startIsPos else -1
        
        left, right = 0, len(A) - 1 
        while left <= right:
            while left <= right and A[left] * flag > 0:
                left += 1 
            while left <= right and A[right] * flag < 0:
                right -= 1 
            
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1 
                right -= 1 
    
    def interleaving(self, A, sameLength):
        if sameLength:
            left, right = 1, len(A) - 2 
        else:
            left, right = 1, len(A) - 1 
            
        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 2 
            right -= 2 