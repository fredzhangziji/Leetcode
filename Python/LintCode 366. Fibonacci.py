class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        fibonacciList = []
        
        for i in range(n):
            if i == 0 or i == 1:
                fibonacciList.append(i)
            else:
                fibonacciList.append(fibonacciList[i - 1] + fibonacciList[i - 2])
                
        return fibonacciList[n-1]