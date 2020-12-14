from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        for i in range(len(nums)):
            if i == 0:
                runningSum.append(nums[i])
            else:
                runningSum.append(runningSum[i-1] + nums[i])
            
        return runningSum