class Solution:
# 这种方法是for循环+记忆
#     def climbStairs(self, n: int) -> int:
#         stepList = []
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
        
#         for i in range(1,n+1):
#             if i == 1:
#                 stepList.append(1)
#             elif i == 2:
#                 stepList.append(2)
#             else:
#                 stepList.append(stepList[i-2]+stepList[i-3])
        
#         return stepList[n-1]


# 递归写法
#     global stepList 
#     stepList = {}
#     def climbStairs(self, n: int) -> int:
        
#         if n <= 1:
#             return 1
        
#         if n not in stepList:
#             stepList[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
#         return stepList[n]


# dp写法
    def climbStairs(self, n: int) -> int:
        # dynamic programming
        dp = [1] * (n+1)
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
            