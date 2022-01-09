from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # https://www.youtube.com/watch?v=w58KFpW5Pjk
        if nums is None or len(nums) == 0:
            return 
        
        replace = len(nums) - 2
        while replace >= 0:
            if nums[replace] < nums[replace+1]:
                break
            replace -= 1
        
        if replace < 0:
            nums.sort()
            return
        
        largerIdx = replace + 1
        while largerIdx < len(nums) and nums[largerIdx] > nums[replace]:
            largerIdx += 1
        
        tmp = nums[replace]
        nums[replace] = nums[largerIdx-1]
        nums[largerIdx-1] = tmp
        nums[replace+1:] = reversed(nums[replace+1:])
        # nums[replace+1:] = sorted(nums[replace+1:])