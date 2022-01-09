class Node():
    def __init__(self, val):
        self.next = None
        self.val = val


class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self, item):
        # write your code here
        if self.first == None:
            self.first = Node(item)
            self.last = self.first
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.first is not None:
            item = self.first.val
            self.first = self.first.next
            return item
        
        else:
            return -1000
        