# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # edge case
        if root.left and not root.right:
            return False
        if not root.left and root.right:
            return False
        if not root.left and not root.right:
            return True
        
        # two bfs queue
        queueL = [root.left]
        queueR = [root.right]
        
        while queueL or queueR:
            if len(queueL) != len(queueR):
                return False
            
            length = len(queueL)
            for _ in range(length):
                cNodeL = queueL.pop(0)
                cNodeR = queueR.pop(0)
                
                if not cNodeL and not cNodeR:
                    continue
                
                if (not cNodeL and cNodeR) or (cNodeL and not cNodeR):
                    return False
                
                if cNodeL and cNodeR:
                    if cNodeL.val != cNodeR.val:
                        return False
                    
                    queueL.append(cNodeL.left)
                    queueL.append(cNodeL.right)
                    queueR.append(cNodeR.right)
                    queueR.append(cNodeR.left)
                    
        return True
