class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        listWord = s.split()
        res = " ".join(listWord[::-1])

        return res 