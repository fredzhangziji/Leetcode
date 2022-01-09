from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        ans = 0
        
        while l < r:
            if max_l < max_r:
                ans += (max_l - height[l])
                l += 1
                max_l = max(height[l], max_l)
                
            else:
                ans += (max_r - height[r])
                r -= 1
                max_r = max(height[r], max_r)
                
        return ans
        
        