class Solution:
    """
    @param string: A string
    @return: whether the string is a valid parentheses
    """
    def matchParentheses(self, string):
        # write your code here
        stack = []

        for ch in string:
            if ch == "(":
                stack.append(")")
            
            else:
                if not stack:
                    return False 
                else:
                    stack.pop()
            
        return not stack