# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # edge case
        if root1 and not root2:
            return root1
        if root2 and not root1:
            return root2
        if not root1 and not root2:
            return root1
        
        queue1 = [root1]
        queue2 = [root2]
        
        while queue1 != [] and  queue2 != []:
            cNode1 = queue1.pop(0)
            cNode2 = queue2.pop(0)
            
            if cNode1 and cNode2:
                cNode1.val = cNode1.val + cNode2.val
                
                if not cNode1.left and cNode2.left:
                    cNode1.left = TreeNode(0)
                if not cNode1.right and cNode2.right:
                    cNode1.right = TreeNode(0)                
                
                queue1.append(cNode1.left)
                queue1.append(cNode1.right)
                queue2.append(cNode2.left)
                queue2.append(cNode2.right)
            
        return root1