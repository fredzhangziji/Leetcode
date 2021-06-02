#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, root):
        if root:
            self.res.append(root.val)
            self.helper(root.left)
            self.helper(root.right)
