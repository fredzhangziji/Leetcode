from typing import List
import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        # 这一题一定要注意枚举的时候要sqrt，能缩短一半时间！否则会超时。
        
        res = []
        for item in nums:
            count = 0
            temp = []
            
            if math.floor(math.sqrt(item)) * math.floor(math.sqrt(item)) == item:
                count += 1
                temp.append(math.sqrt(item))
            for i in range(1,math.floor(math.sqrt(item))+1):
                if item % i == 0:
                    count += 2
                    if count <= 4:
                        temp.append(i)
                        temp.append(item//i)
                    if count > 4:
                        break
            if count == 4:
                for tmp in temp:
                    res.append(tmp)
                    
        return int(sum(res)) 
            
            