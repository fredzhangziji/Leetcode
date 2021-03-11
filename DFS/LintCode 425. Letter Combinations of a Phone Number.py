# comment掉的是有backtracking的写法
KEYBOARD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
        
        result = []
        # self.dfs(digits, 0, [], result)
        self.dfs(digits, 0, "", result)
        return result

    def dfs(self, digits, index, char, result):
        if index == len(digits):
            # result.append(''.join(char))
            result.append(char)
            return 
        
        for letter in KEYBOARD[digits[index]]:
            # char.append(letter)
            self.dfs(digits, index + 1, char + letter, result)
            # char.pop()