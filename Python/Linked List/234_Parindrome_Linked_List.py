# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = []
        while head is not None:
            tmp.append(head.val)
            head = head.next
            
        return tmp == tmp[::-1]