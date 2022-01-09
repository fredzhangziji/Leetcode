class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here
        res = self.decToBi(n)
        left = 0
        newN = str(res)
        right = len(newN) - 1

        while left < right:
            if newN[left] != newN[right]:
                return False 
            
            left += 1
            right -= 1
        
        return True

    def decToBi(self, num):
        res = 0
        index = 1
        while num != 0:
            res += num % 2 * index
            index *= 10
            num //= 2

        return res
