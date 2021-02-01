"""
Definition of TreeNode:
"""
import collections
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


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

#     def levelOrder(self, root):
#         # write your code here
#         if not root:
#             return []
        
#         # 双队列
#         queue = [root]
#         res = []
        
#         while queue:
#             next_queue = []
#             tmpres = []
#             for _ in range(len(queue)):
#                 currNode = queue.pop(0)
#                 tmpres.append(currNode.val)
#                 if currNode.left:
#                     next_queue.append(currNode.left)
#                 if currNode.right:
#                     next_queue.append(currNode.right)
#             queue = next_queue
#             res.append(tmpres)
        
#         return res