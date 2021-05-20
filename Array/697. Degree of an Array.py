from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        dict1 = {}
        for index, num in enumerate(nums):
            if num in dict1:
                dict1[num].append(index)
            if num not in dict1:
                dict1[num] = [index]
        
        maxF = 0
        minLen = float('inf')
        print(dict1)
        for key in dict1:
            
            if len(dict1[key]) > maxF:
                maxF = len(dict1[key])
                minLen = max(dict1[key]) - min(dict1[key]) + 1
            
            if len(dict1[key]) == maxF and max(dict1[key]) - min(dict1[key]) + 1 < minLen:
                maxF = len(dict1[key])
                minLen = max(dict1[key]) - min(dict1[key]) + 1
            
        return minLen
        