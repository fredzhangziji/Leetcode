class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        
        if not S:
            return S 
        
        S.sort()
        count = 0
        
        for i in range(len(S)):
            left, right = 0, i - 1 
            
            while left < right:
                if S[left] + S[right] > S[i]:
                    count += right - left
                    right -= 1 
                elif S[left] + S[right] <= S[i]:
                    left += 1
        
        return count 