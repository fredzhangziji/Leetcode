# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
# 这个方法的时间复杂度和空间复杂度都是O(n)
#         nums = []
#         while head:
#             nums.append(head.val)
#             head = head.next
        
#         res = 0
#         count = 0
#         for num in reversed(nums):
#             res += num*2**count
#             count += 1
#         return res

# 这个方法的时间复杂度是O(n)，但是空间复杂度是O(1)
        res = 0
        while head:
            res = res*2 + head.val
            head = head.next

        return res