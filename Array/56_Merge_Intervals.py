from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # https://www.youtube.com/watch?v=6tLHjei-f0I
        ans = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans