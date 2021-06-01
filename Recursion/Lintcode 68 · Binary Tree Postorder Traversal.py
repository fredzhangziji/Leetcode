#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    
    def postorderTraversal(self, root):
        # write your code here
        self.res = []
        self.recursion(root)
        return self.res


    def recursion(self, root):
        if root:
            self.recursion(root.left)
            self.recursion(root.right)
            self.res.append(root.val)
        