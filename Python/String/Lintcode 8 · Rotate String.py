class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if not s:
            return

        offset %= len(s)
        
        '''
         "abcdefg"
         offset = 3
         "efgabcd"
         lenX = 7 - 3 = 4
         reverse: 0-3; 4-6. -> 两段分别原地翻转
         reverse: 0-6 -> 整段原地翻转
        '''
        lenX = len(s) - offset
        self.reverse(s, 0, lenX -1)
        self.reverse(s, lenX, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)

        '''
        "abcdefg"
        "cbagfed"
        "defgabc"
        '''

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1