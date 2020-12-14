from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        numStudent = max(items)[0]
        res = []
        
        while items:
            Id = items[0][0]
            tmpList = []
            j = 0
            for _ in range(len(items)):
                if items[j][0] == Id:
                    tmpList.append(items[j][1])
                    items.pop(j)
                else:
                    j += 1
            tmpRes = []
            for k in range(5):
                tmpRes.append(max(tmpList))
                tmpList.remove(max(tmpList))
            tmpAvg = int(sum(tmpRes)/5)
            res.append([Id,tmpAvg])
        
        return sorted(res)