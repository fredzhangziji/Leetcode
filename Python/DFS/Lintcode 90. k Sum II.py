class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        A = sorted(A)
        result = []
        self.dfs(A, result, k, target, [], 0)
        return result

    def dfs(self, A, result, k, target, combination, start):
        if k < 0:
            return
        
        if k == 0:
            if target < 0:
                return 
            if target == 0:
                result.append(list(combination))
        
        for i in range(start, len(A)):
            combination.append(A[i])
            self.dfs(A, result, k - 1, target - A[i], combination, i + 1)
            combination.pop()