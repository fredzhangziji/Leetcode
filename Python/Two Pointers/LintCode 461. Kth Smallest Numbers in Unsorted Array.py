class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        return self.partition(0, len(nums) - 1, nums, k - 1)
        
    def partition(self, start, end, nums, k):
        left, right = start, end
        pivot = nums[left]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        
        if left <= k and left <= end:
            return self.partition(left, end, nums, k)
        elif right >= k and right >= start:
            return self.partition(start, right, nums, k)
        else:
            return nums[k]