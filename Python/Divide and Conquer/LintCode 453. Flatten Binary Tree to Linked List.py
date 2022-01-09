"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.return_last_node(root)
        
    def return_last_node(self, root):
        # 出口
        if root is None:
            return None
            
        left_last = self.return_last_node(root.left)
        right_last = self.return_last_node(root.right)
        
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        
        return right_last or left_last or root