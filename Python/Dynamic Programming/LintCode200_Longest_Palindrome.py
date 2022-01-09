class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        
        # use Dynamic Programming
        
        # corner cases:
        if not s: # not s means s is None or s is ""
            return s 
            
        n = len(s)
        
        # create a n*n 2-d array
        is_palindrome = [[False] * n for _ in range(n)]
        
        # initialize the dp 2-d array
        for i in range(n):
            # single letter must be a palindrom
            is_palindrome[i][i] = True
        for i in range(1, n):
            # empty string is also a palindrome
            is_palindrome[i][i-1] = True
            
        start, longest = 0, 1 
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1 
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
                if is_palindrome[i][j] and length > longest:
                    longest = length
                    start = i
        
        return s[start: start + longest]