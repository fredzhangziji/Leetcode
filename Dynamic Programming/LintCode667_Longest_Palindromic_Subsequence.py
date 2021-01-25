class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        
        # dp Solution
        size = len(s)
        
        # corner case 
        if size <= 1: 
            return size
        
        # intialize the dp 2-d array 
        # the dp array means the length of the longest palindromic subsequence from i to j 
        dp = [[0] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1
            
        for i in range(size-1, -1, -1):
            for j in range(i + 1, size):
                if s[i] == s[j]: # when s[i] == s[j] 
                    dp[i][j] = dp[i + 1][j - 1] + 2 
                else: # when s[i] != s[j]
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        
        return dp[0][size-1]