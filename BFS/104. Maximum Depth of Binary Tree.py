# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # edge case
        if not root:
            return 0
        
        queue = [root]
        maxDepth = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                cNode = queue.pop(0)
                
                if cNode.left:
                    queue.append(cNode.left)
                    
                if cNode.right:
                    queue.append(cNode.right)
                    
            maxDepth += 1
        
        return maxDepth