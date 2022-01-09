from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for num in nums:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1
            
        
        for num in nums:
            val = target - num
            if val == num:
                if numsDict[val] == 2:
                    return [nums.index(num), nums.index(num,nums.index(num)+1)]
            else:
                if val in numsDict:
                    return [nums.index(num), nums.index(val)]