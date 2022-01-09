import sys

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        
        character = {}
        for char in s:
            if char in character:
                character[char] += 1
            if char not in character:
                character[char] = 1
        
        nonR = []
        for char, count in character.items():
            if count == 1:
                nonR.append(char)
        
        if nonR == []:
            return -1
        
        minIdx = sys.maxsize
        for char in nonR:
            minIdx = min(minIdx, s.index(char))
        
        return minIdx