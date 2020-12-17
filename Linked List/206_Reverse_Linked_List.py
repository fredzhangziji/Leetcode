# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        tmp = []
        while head is not None:
            tmp.append(head.val)
            head = head.next
        
        res = ListNode()
        current = res
        tmp.reverse()
        for i in range(len(tmp)):
            if i != len(tmp)-1:
                current.val = tmp[i]
                current.next = ListNode()
                current = current.next
            else:
                current.val = tmp[i]
                
            
        return res