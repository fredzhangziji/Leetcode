class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n < 1 or n > len(nums):
            return None 
        return self.partition(len(nums) - n, nums, 0, len(nums) - 1)
        
    
    
    def partition(self, n, nums, start, end):
        """
        During the process, it's guaranteed start <= k <= end
        """
        # corner case 
        if start == end:
            return nums[n]
            
        pivot = nums[(end + start) // 2]
        
        left, right = start, end
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
            
        if n <= right:
            return self.partition(n, nums, start, right)
        
        if n >= left:
            return self.partition(n, nums, left, end)
                
        return nums[n]
