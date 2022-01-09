from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
    
        def helper(term, idx):
            if idx == len(nums):
                return term
            
            return helper(term, idx + 1) + helper(term ^ nums[idx], idx + 1)
        
        return helper(0, 0)