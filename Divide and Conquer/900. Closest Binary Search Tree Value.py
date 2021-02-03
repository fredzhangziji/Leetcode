"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        upper = root 
        lower = root
        
        while root:
            if target < root.val:
                upper = root
                root = root.left
            
            elif target > root.val:
                lower = root
                root = root.right
            
            else:
                return root.val
                
        if abs(upper.val - target) <= abs(target - lower.val): 
            # 这里加abs是为了防止target小于最小值或者target大于最大值
            return upper.val
            
        return lower.val
            