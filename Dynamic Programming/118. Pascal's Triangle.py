from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # creat a dp table and initialize it
        dp = [[1] * numRows for _ in range(numRows)]
        
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        result = []
        for i in range(numRows):
            result.append(dp[i][:i+1])
            
        return result
