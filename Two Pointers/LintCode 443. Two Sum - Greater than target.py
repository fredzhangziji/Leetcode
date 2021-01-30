class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        
        if not nums:
            return 0
        
        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1 
        while left < right:
            if left < right and nums[left] + nums[right] > target:
                ans += right - left
                right -= 1 
            if left < right and nums[left] + nums[right] <= target:
                left += 1 
        
        return ans