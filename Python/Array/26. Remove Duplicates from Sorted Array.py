from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        second = 1
        
        while second < len(nums):
            if nums[first] == nums[second]:
                nums.pop(second)
            else:
                first += 1
                second += 1

        return len(nums)