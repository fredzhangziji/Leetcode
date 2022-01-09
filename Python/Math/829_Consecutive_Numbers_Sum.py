import math
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # Find the nubmer of odd factors
        # It's just magic...
        
        count = 0
        for i in range(1,math.floor(math.sqrt(N)+1)):
            if N%i == 0:
                if i%2:
                    count+=1
                if N/i != i and (N/i)%2:
                    count+=1
        return count