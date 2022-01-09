from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            tmp = s[j] 
            s[j] = s[i]
            s[i] = tmp
            
            i += 1 
            j -= 1
        