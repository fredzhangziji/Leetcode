class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def returnString(Z: str) -> str:
            skip = 0
            i = len(Z) - 1
            res = ""
            while i >= 0:
                if Z[i] == "#":
                    skip += 1
                    i -= 1
                elif skip:
                    i -= 1
                    skip -= 1
                else:
                    res += Z[i]
                    i -= 1
                    
            return res[::-1]
        
        return returnString(S) == returnString(T)
                    