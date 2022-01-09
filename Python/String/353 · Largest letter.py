class Solution:
    """
    @param s: a string
    @return: a string
    """
    def largestLetter(self, s):
        # write your code here
        lowerCase = [0] * 26
        upperCase = [0] * 26

        for char in s:
            if char.islower():
                lowerCase[ord(char) - ord('a')] += 1 
            else:
                upperCase[ord(char) - ord('A')] += 1
        
        for i in range(-1, -27, -1):
            if lowerCase[i] != 0 and upperCase[i] != 0:
                return chr(ord('Z') + i + 1) 
        
        return "NO"