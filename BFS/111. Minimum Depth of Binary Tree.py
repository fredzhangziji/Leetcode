# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # edge case
        if not root:
            return 0
        
        queue = [root]
        minDepth = 0
        
        while queue:
            minDepth += 1
            length = len(queue)
            for _ in range(length):
                cNode = queue.pop(0)
                if not cNode.left and not cNode.right:
                    return minDepth
                
                if cNode.left:
                    queue.append(cNode.left)
                if cNode.right:
                    queue.append(cNode.right)
                    
            
        