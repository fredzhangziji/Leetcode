from typing import List
# Create a dictionary for the char-to-num mapping.
KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'    
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        res = []
        self.dfs(digits, 0, "", res)
        return res
        
        
    def dfs(self, digits, idx, char, res):
        # When to stop (base case):
        # when the dfs reaches the last digits, we add the current char into the res, and return.
        if idx == len(digits):
            res.append(char)
            return 
        
        # DFS
        for letter in KEYBOARD[digits[idx]]:
            self.dfs(digits, idx + 1, char + letter, res)