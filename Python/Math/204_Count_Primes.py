class Solution:
    def countPrimes(self, n: int) -> int:
        # sieve 
        if n < 3:
            return 0
        
        isPrime = [True] * (n+1)
        isPrime[0] = False
        isPrime[1] = False
        
        res = 0
        for i in range(2,n):
            if not isPrime[i]:
                continue
            else:
                for j in range(i*i, n, i):
                    isPrime[j] = False
                res += 1
        
        return res
