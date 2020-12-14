from typing import List

class Solution:
    def fib(self, N: int) -> int:
        F = []
        for i in range(N+1):
            if i == 0:
                F.append(0)
            elif i == 1:
                F.append(1)
            else:
                F.append(F[i-1] + F[i-2])
        
        return F[N]