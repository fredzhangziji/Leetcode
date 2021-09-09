# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # edge case
        if not root:
            return False
        
        queue = [root]
        element = set()
        
        while queue:
            cNode = queue.pop(0)
            if k - cNode.val in element:
                return True
            element.add(cNode.val)
            
            if cNode.left:
                queue.append(cNode.left)
            if cNode.right:
                queue.append(cNode.right)
        
        return False