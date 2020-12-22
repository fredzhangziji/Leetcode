class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        else:
            p1 = 0
            p2 = len(s) - 1
            while p1 < p2:
                if s[p1] == s[p2]:
                    p1 += 1
                    p2 -= 1
                else:
                    if s[p1+1:p2+1] == s[p2:p1:-1]:
                        return True
                    elif s[p1:p2] == s[p2-1:p1-1 if p1>0 else None:-1]:
                        return True
                    else:
                        return False