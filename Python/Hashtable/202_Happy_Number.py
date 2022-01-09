class Solution:
    def isHappy(self, n: int) -> bool:
        resSum = 0
        sumTable = {}
        
        nStr = str(n)
        for digit in nStr:
            resSum += int(digit) * int(digit)
        
        if resSum == 1:
            return True
        
        sumTable[resSum] = 1
        
        while resSum != 1:
            nStr = str(resSum)
            resSum = 0
            for digit in nStr:
                resSum += int(digit) * int(digit)
            
            if resSum in sumTable:
                return False
            
            sumTable[resSum] = 1
                
            
        return True
            