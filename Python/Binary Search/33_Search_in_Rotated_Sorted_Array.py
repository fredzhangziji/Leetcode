from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (begin+end) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[end]: # Left side of mid is sorted
                if nums[begin] <= target and target < nums[mid]: # Target in the left side
                    end = mid - 1
                else: # Target in the right side
                    begin = mid + 1
            
            else: # Right side of mid is sorted
                if nums[mid] < target and target <= nums[end]: # Target in the right side
                    begin = mid + 1
                else: # Target in the left side
                    end = mid - 1
        
        # Target doesn't exist in the list
        return -1