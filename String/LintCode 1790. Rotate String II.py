class Solution:
    """
    @param str: A String
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        
        if left == right:
            return str
        
        elif left > right:
            res = (left - right) % len(str)
            str = str[res:] + str[:res]
            
        elif left < right:
            res = (right - left) % len(str)
            str = str[len(str) - res:] + str[:len(str) - res]
            
        return str