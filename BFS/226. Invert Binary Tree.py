# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # edge case
        if not root:
            return root
        
        queue = [root]
        
        while queue:
            cNode = queue.pop(0)
            if cNode:
                cNode.left, cNode.right = cNode.right, cNode.left
                queue.append(cNode.left)
                queue.append(cNode.right)
                
        return root
            