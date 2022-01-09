# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        prev = head
        curr = head.next
        
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
        
        return head
            