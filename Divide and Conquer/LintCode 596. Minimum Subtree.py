import sys
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        sum, min_sum, min_subtree = self.divideAndConquer(root)
        return min_subtree
        
    def divideAndConquer(self, root):
        # exit
        if root is None:
            return sys.maxsize, sys.maxsize, None
        
        # 分治：算出左右子树的和、最小和、最小节点
        left_sum, min_left_sum, min_left_subtree = self.divideAndConquer(root.left)
        right_sum, min_right_sum, min_right_subtree = self.divideAndConquer(root.right)
        
        min_sum = sys.maxsize
        sum = root.val # sum是指当前子树的和
        if root.left:
            sum += left_sum # 所以要加的是左子树整棵树的和
        if root.right:
            sum += right_sum # 所以要加的是右子树整棵树的和
        # sum是当前子树和，min_left_sum是当前子树的左子树和，min_right_sum是当前子树的右子树和
        min_sum = min(min_left_sum, min_right_sum, sum)
        
        # 更新完这些sum之后，判断一下哪个最小，然后返回这个节点
        if min_sum == sum: # 说明当前节点最小
            return sum, min_sum, root
        if min_sum == min_left_sum: # 说明最小节点在左子树里（不一定是左子树这个节点，可能是他的儿子）
            return sum, min_sum, min_left_subtree 
        return sum, min_sum, min_right_subtree # 说明最小节点在 右子树里（不一定是右子树这个节点，可能是他的儿子）