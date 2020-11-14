import collections
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # 思路：dfs+bfs
        # dfs来找到最深的节点的column index（一个左边，一个右边）
        # bfs来遍历每一层的节点

        def dfs(root: TreeNode, index: int):
            
            global minIndex
            global maxIndex
            # base case
            if not root:
                return

            # update minIndex and maxIndex whenever dfs() is called
            minIndex = min(index, minIndex)
            maxIndex = max(index, maxIndex)

            dfs(root.left, index-1)
            dfs(root.right, index+1)
            
            
        # base case
        if not root:
            return []
        
        global minIndex
        global maxIndex
        minIndex = 0
        maxIndex = 0
        dfs(root, 0) # 调用dfs来找到最小的colume index和最大的colume index（最左边和最右边）
        
        # 把答案的list构建好，这样之后就只需要往对应的位置加答案就行了
        res = []
        for i in range(minIndex, maxIndex+1):
            res.append([])
        
        queue = collections.deque() # 创建queue为bfs作准备
        queue.append(root)
        indexQueue = collections.deque() # 这个queue是来存index的，每次pop一个节点，就把这个对应的index加进去
        indexQueue.append(-minIndex) # 这边push这个是因为root对应的index应该是最左边的那个index的绝对值（offset）
        while queue:
            currNode = queue.popleft()
            currIndex = indexQueue.popleft()
            # 加入答案list
            res[currIndex].append(currNode.val)
            
            if currNode.left:
                queue.append(currNode.left)
                indexQueue.append(currIndex-1)
            
            if currNode.right:
                queue.append(currNode.right)
                indexQueue.append(currIndex+1)
                
        return res