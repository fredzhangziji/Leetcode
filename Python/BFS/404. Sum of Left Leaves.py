# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # edge case
        if not root:
            return 0
        
        queue = [root]
        leftSum = 0
        
        while queue:
            cNode = queue.pop(0)
            if cNode.left:
                queue.append(cNode.left)
                if not cNode.left.left and not cNode.left.right:
                    leftSum += cNode.left.val
            if cNode.right:
                queue.append(cNode.right)
                
        return leftSum
        