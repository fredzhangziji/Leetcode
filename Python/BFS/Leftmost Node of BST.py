class Node:
      def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
      

def printLeftMost(root):

      # check edge case
      if root == None:
            return 

      queue = []
      queue.append(root)
      res = []

      while queue:
            n = len(queue)
            for i in range(n):
                  tmpNode = queue[0]
                  queue.pop(0)
                  if i == 0:
                        res.append(tmpNode.val)
                  
                  if tmpNode.left:
                        queue.append(tmpNode.left)
                  if tmpNode.right:
                        queue.append(tmpNode.right)
      
      return res


if __name__ == "__main__":
      root = Node(15)
      root.left = Node(10)
      root.right = Node(20)
      root.left.left = Node(8)
      root.left.right = Node(12)
      root.right.left = Node(16)
      root.right.right = Node(25)
      print(printLeftMost(root))


