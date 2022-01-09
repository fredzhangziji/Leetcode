# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # edge case
        if not root:
            return root
        
        queue = [root]
        result = []
        
        while queue:
            size = len(queue)
            nodeSum = 0
            for _ in range(size):
                cNode = queue.pop(0)
                nodeSum += cNode.val
                if cNode.left:
                    queue.append(cNode.left)
                if cNode.right:
                    queue.append(cNode.right)
                    
            result.append(nodeSum/size)
            
        return result
                    
                