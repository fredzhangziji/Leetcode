#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        _, diameter = self.helper(root)
        return diameter
    

    def helper(self, root):
        # base case 
        if not root:
            return (0, 0)
        
        left_longest, left_diameter = self.helper(root.left)
        right_longest, right_diameter = self.helper(root.right)

        # 对于这个节点的longest，要么是左子树连着它，要么是右子树连着它
        longest = max(left_longest + 1, right_longest + 1)

        # 对于这个节点的最长diameter，要么在左子树里，要么在右子树里，要么是
        # 更新的版本，就是左子树的longest单链和右子树的longest单链连起来
        diameter = max(left_diameter, right_diameter, left_longest + right_longest)

        return longest, diameter

