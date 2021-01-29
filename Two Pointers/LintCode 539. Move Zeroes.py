class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        
        if not nums:
            return nums
        
        # left means the pointer for the new list
        # right means the pointer for the old list
        # then we start to scan (move the pointer)
        left, right = 0, 0
        
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                right += 1 
                left += 1 
            else: # nums[right] == 0
                right += 1
        
        if left < len(nums):
            for i in range(left, len(nums)):
                nums[i] = 0
                
        return nums