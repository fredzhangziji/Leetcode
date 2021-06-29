# Leetcode 20
class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        if len(s) % 2 != 0:
            return False

        stack = []
        for ch in s:
            if ch == "(":
                stack.append(")")
            elif ch == "[":
                stack.append("]")
            elif ch == "{":
                stack.append("}")
            
            else:
                if not stack or stack.pop() != ch:
                    return False 
        
        return not stack  