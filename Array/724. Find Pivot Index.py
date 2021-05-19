from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # prefix sum: 如果我们算到了pivot之前的prefix sum，根据题目的性质，那sum - prefix sum - pivot肯定等于prefix sum。
        Sum = sum(nums)
        prefixSum = 0
        
        for i in range(len(nums)):
            if Sum - prefixSum - nums[i] == prefixSum:
                return i
            
            prefixSum += nums[i]
        
        return -1
                

# this solution is very very slow
# this is O(n^2)
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
        
#         if not nums:
#             return -1
        
#         for pivot in range(len(nums)):
#             if sum(nums[:pivot]) == sum(nums[pivot+1:]):      
#                 return pivot
        
#         return -1


                