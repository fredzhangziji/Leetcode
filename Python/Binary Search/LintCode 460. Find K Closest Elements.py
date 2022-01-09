class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        res = []
        right = self.findTarget(A, target)
        left = right - 1 
        while k > 0:
            if self.isLeftBigger(A, target, left, right):
                res.append(A[left])
                left -= 1 
                k -= 1 
            else:
                res.append(A[right])
                right += 1 
                k -= 1 
        return res
        
    
    def findTarget(self, A, target):
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = (start + end) // 2 
            if A[mid] >= target:
                end = mid 
            else:
                start = mid
            
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end 
        return len(A)
        
        
    def isLeftBigger(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        
        if target - A[left] <= A[right] - target:
            return True
        else:
            return False
        