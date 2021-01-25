class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        
        # corner case
        if s == "":
            return True
        
        left = 0
        right = len(s) - 1 
        while left <= right:
            if s[left] == s[right]:
                left += 1 
                right -= 1 
            else:
                return self.helper(s, left + 1, right) or self.helper(s, left, right - 1)
            
        return True
        
    def helper(self, s, left, right):
        while left <= right:
            if s[left] == s[right]:
                left += 1 
                right -= 1 
            else: 
                return False
                
        return True
