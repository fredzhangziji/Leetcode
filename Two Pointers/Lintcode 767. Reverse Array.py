class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        # write your code here
        left = 0
        right = len(nums) - 1 
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        
        return nums