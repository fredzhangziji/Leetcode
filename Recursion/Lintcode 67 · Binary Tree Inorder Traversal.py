#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        self.res = []
        self.helper(root)
        return self.res
    

    def helper(self, root):

        if root:
            self.helper(root.left)
            self.res.append(root.val)
            self.helper(root.right)
