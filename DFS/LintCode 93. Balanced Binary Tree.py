"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        isBalanced, _ = self.divideAndConquer(root)
        return isBalanced
        
    def divideAndConquer(self, root):
        
        if root is None:
            return True, 0
            
        leftIsBalanced, leftHeight = self.divideAndConquer(root.left)
        rightIsBalanced, rightHeight = self.divideAndConquer(root.right)
        rootHeight = max(leftHeight, rightHeight) + 1 

        if not leftIsBalanced or not rightIsBalanced:
            return False, rootHeight
        
        if abs(leftHeight - rightHeight) > 1:
            return False, rootHeight
        
        return True, rootHeight
        
        