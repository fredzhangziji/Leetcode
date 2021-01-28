class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        
        # corner case:
        if not nums:
            return 0
        
        nums.sort()
        ans = 0
        left = 0
        right = len(nums) - 1 
        while left < right:
            while left != 0 and nums[left] == nums[left - 1]:
                left += 1 
            while right != len(nums) - 1 and nums[right] == nums[right + 1]:
                right -= 1 
            
            if left < right:
                if nums[left] + nums[right] == target:
                    ans += 1 
                    left += 1 
                    right -= 1 
                elif nums[left] + nums[right] < target:
                    left += 1 
                else: 
                    right -= 1 
        
        return ans