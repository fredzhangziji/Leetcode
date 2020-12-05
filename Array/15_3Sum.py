from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == [] or nums == [0]:
            return []
        
        
        dictNum = {}
        for element in nums:
            if element in dictNum:
                dictNum[element] += 1
            if element not in dictNum:
                dictNum[element] = 1
            
        res = set()
        
        for element in dictNum:
            # 注意这里要用copy来搞一个新的dictionary，不然就是assign by reference
            tempDict = dictNum.copy()
            if tempDict[element] != 0:
                twoSum = 0 - element
                tempDict[element] -= 1
                for element2 in tempDict:
                    if tempDict[element2] != 0:
                        oneSum = twoSum - element2
                        tempDict[element2] -= 1
                        if oneSum in tempDict and tempDict[oneSum] != 0:
                            tempList = [element, element2, oneSum]
                            tempList.sort()
                            tempTuple = tuple(tempList)
                            res.add(tempTuple)
                            
        res = list(res)
        
        return res
