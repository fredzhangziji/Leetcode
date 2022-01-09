# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp = []
        while head:
            tmp.append(head)
            head = head.next
        
        lenTmp = len(tmp)
        if lenTmp % 2 == 1:
            idx = lenTmp // 2
        else:
            idx = lenTmp // 2
        
        return tmp[idx]