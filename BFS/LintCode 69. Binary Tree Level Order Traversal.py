"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
            
        queue = collections.deque([root])
        res = []
        
        while queue:
            tmpres = []
            for _ in range(len(queue)):
                currNode = queue.popleft()
                tmpres.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            res.append(tmpres)
            
        return res