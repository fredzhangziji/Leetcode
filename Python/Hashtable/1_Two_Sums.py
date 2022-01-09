from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNum = {}
        for num in nums:
            if num in dictNum:
                dictNum[num] += 1
            else: 
                dictNum[num] = 1
        
        for num in nums:
            value = target - num
            if value in dictNum:
                if value == num:
                    if dictNum[value] == 2:
                        return nums.index(value), nums.index(value, nums.index(value)+1)
                    else: continue
                return nums.index(num), nums.index(value)