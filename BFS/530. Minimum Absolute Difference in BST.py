# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # edge case
        if not root:
            return root
        
        queue = [root]  # bfs queue
        vals = [] # list for the elements
        diff = float('inf') # initialize the diff as max num
        
        while queue:
            cNode = queue.pop(0)
            vals.append(cNode.val)
            
            if cNode.left:
                queue.append(cNode.left)
            
            if cNode.right:
                queue.append(cNode.right)
            
        vals.sort() # sort the list
        
        for i in range(len(vals)-1): # -1 because we are comparing in pairs
            if abs(vals[i] - vals[i+1]) < diff:
                diff = abs(vals[i] - vals[i+1])
                
        return diff