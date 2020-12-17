# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        table = {}
        while headA:
            if headA not in table:
                table[headA] = 1
            headA = headA.next
            
        
        while headB:
            if headB in table:
                return headB
            headB = headB.next
            
        return None