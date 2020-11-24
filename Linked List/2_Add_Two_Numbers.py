# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 个位数
        remain = 0
        val = l1.val + l2.val
        if val < 10:
            res = ListNode(val)
        else:
            res = ListNode(val%10)
            remain = val // 10
        current = res
        
        while l1.next or l2.next or remain:
            
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            
            val = l1.next.val + l2.next.val + remain
            l1 = l1.next
            l2 = l2.next
            if val < 10:
                current.next = ListNode(val)
                current = current.next
                remain = 0
                
            else:
                current.next = ListNode(val%10)
                remain = val // 10
                current = current.next
        return res
        