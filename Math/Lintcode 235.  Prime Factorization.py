import math

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        res = []
        for i in range(2, math.ceil(math.sqrt(num))+1):
            while num % i == 0:
                res.append(i)
                num = num // i
        
        if num > 1:
            res.append(num)
        return res
