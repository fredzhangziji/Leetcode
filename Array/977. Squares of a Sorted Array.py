from typing import List

# sort version: kinda cheat
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             nums[i] = nums[i] * nums[i]
        
#         return sorted(nums)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = len(nums) - 1
        result = []
        
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[right] * nums[right])
                right -= 1
                
            else:
                result.append(nums[left] * nums[left])
                left += 1
            
        return result[::-1]