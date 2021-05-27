class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        # Write your code here

        # check the first one:
        n = len(s)

        # make every character an element in the list
        s1 = list(s)

        if s1[0] >= 'a' and s1[0] <= 'z':
            s1[0] = s1[0].upper()

        # check the one after the space
        for i in range(1, n):
            if s1[i-1] == ' ' and s1[i] != ' ':
                s1[i] = s1[i].upper()

        return ''.join(s1)
