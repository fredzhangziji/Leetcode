class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def canWinBash(self, n):
        # Write your code here
        '''
        4 % 4 = 0 False
        5 % 4 = 1 True 
        6 % 4 = 2 True 
        7 % 4 = 3 True 
        8 % 4 = 0 False 
        '''

        return False if n % 4 == 0 else True