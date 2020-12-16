from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)):
            length1 = len(words[i])
            for j in range(i+1, len(words)):
                length2 = len(words[j])
                if length2 < length1 and words[i][:length2] == words[j][:length2]:
                    return False
                for k in range(length1):
                    if order.index(words[i][k]) > order.index(words[j][k]):
                        return False
                    elif order.index(words[i][k]) < order.index(words[j][k]):
                        break
        return True