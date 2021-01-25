class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        # 基于中心线枚举的算法
        # n个奇数长度的回文串中心点
        # n-1个偶数长度的回文串的中心
        
        # 边界检测
        if not s:
            return s
        
        # create a tuple (first element is the length, second element is the start index)
        answer = (0, 0)
        
        # start to iterate the middle point thru the string
        for mid in range(len(s)):
            # odd
            answer = max(answer, self.get_palindrome_from(s, mid, mid))
            # even
            answer = max(answer, self.get_palindrome_from(s, mid, mid + 1))
        
        return s[answer[1]: answer[0] + answer[1]]
        
    def get_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1 
            right += 1 
        
        return right - left - 1, left + 1
        