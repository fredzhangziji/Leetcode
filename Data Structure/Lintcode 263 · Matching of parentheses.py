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


# class Solution:
#     """
#     @param string: A string
#     @return: whether the string is a valid parentheses
#     """
#     def matchParentheses(self, string):
#         # write your code here
#         num_p = 0

#         for ch in string:
#             if ch == "(":
#                 num_p += 1
#             elif ch == ")":
#                 num_p -= 1
            
#             if num_p < 0:
#                 return False 
        
#         return num_p == 0