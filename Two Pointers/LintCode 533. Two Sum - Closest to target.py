class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        
        if not nums:
            return nums
            
        nums.sort()
        
        left = 0
        right = len(nums) - 1 
        minDiff = float('inf')
        
        while left < right:
            if nums[left] + nums[right] < target:
                minDiff = min(minDiff, target - nums[left] - nums[right])
                left += 1 
                
            elif nums[left] + nums[right] > target:
                minDiff = min(minDiff, nums[left] + nums[right] - target)
                right -= 1
                
            else:
                return 0
        
        return minDiff