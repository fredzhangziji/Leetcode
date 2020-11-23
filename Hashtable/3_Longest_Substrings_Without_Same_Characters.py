from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {}
        maxlength = 0
        start = 0
        
        for i, value in enumerate(s):
            if value in dicts:  # 重复了，那这个substring到这之前是valid的
                newStart = dicts[value] + 1 # 把新的起点设置为之前起点的+1
                if newStart > start: # 如果新的起点是在旧起点之后的，我们更新这个起点，因为这代表新起点之后的重复了
                                     # 如果新的起点是在旧起点之前，那么说明我们不用管这个新起点，因为已经pass掉了
                    start = newStart
                    
            num = i - start + 1
            if num > maxlength: # 更新substring的最大长度
                maxlength = num
            dicts[value] = i
        
        return maxlength