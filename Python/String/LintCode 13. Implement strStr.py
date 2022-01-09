class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if not target:
            return 0
        if not source:
            return -1

        
        length = len(target)
        
        for i in range(len(source) - length + 1):
            if source[i:i + length] == target:
                return i
        
        return -1