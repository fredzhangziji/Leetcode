# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # edge case
        if not p and not q: # [] and []
            return True
        if not p and q:  # [] and [0]
            return False
        if p and not q:  # [0] and []
            return False
        
        # bfs for two trees
        # initialize the bfs with the root
        queue1 = [p]
        queue2 = [q]
        
        while queue1 and queue2:
            # check if the structures of the two trees are the same
            if len(queue1) != len(queue2):
                return False
            
            length = len(queue1)
            for _ in range(length):
                cNode1 = queue1.pop(0)
                cNode2 = queue2.pop(0)
                
                if (cNode1 and not cNode2) or (not cNode1 and cNode2):
                    return False
                if not cNode1 and not cNode2:
                    continue
                
                if cNode1.val != cNode2.val:
                    return False
                
                queue1.append(cNode1.left)
                queue2.append(cNode2.left)
                queue1.append(cNode1.right)
                queue2.append(cNode2.right)

        # if everything is equal
        return True