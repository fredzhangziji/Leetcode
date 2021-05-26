class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        length = len(A)
        B = []

        f = [0 for i in range(length + 1)]
        f[length] = 1

        # 从右往左
        for i in range(length - 1, 0, -1):
            f[i] = f[i+1] * A[i]
        
        tmp = 1
        
        # 从左往右
        for i in range(length):
            B.append(tmp * f[i+1])
            tmp *= A[i]
        
        return B