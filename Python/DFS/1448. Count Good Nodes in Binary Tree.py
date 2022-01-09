# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        return self.dfs(root, root.val)
    
    def dfs(self, root, maxVal):
        if not root:
            return 0
        
        maxVal = max(root.val, maxVal)
        if root.val >= maxVal:
            addOrNo = 1
        else:
            addOrNo = 0
        
        addOrNo += self.dfs(root.left, maxVal)
        addOrNo += self.dfs(root.right, maxVal)
        return addOrNo