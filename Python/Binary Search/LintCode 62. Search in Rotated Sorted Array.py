class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        
        if not A:
            return -1 
            
        minIdx = self.findMin(A)
        if A[minIdx] <= target <= A[len(A) - 1]: # target is on the right of the minIdx
            return self.binarySearch(A, minIdx, len(A) - 1, target)
        else: # target is on the left of the minIdx
            return self.binarySearch(A, 0, minIdx - 1, target)
            
    def findMin(self, A):
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = (start + end) // 2 
            if A[mid] < A[end]:
                end = mid 
            elif A[mid] > A[start]:
                start = mid
        
        if A[start] < A[end]:
            return start
        else:
            return end
    
    def binarySearch(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2 
            if A[mid] > target:
                end = mid
            elif A[mid] <= target:
                start = mid 
            else:
                return mid
                
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1
                