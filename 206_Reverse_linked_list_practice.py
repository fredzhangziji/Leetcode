# First, create a class to define linked list
class ListNode:
      def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

# Second, write the function
class Solution:
      def reverseList1(self, head: ListNode) -> ListNode:

            # If nothing, then return nothing
            if head is None:
                  return None
            
            # Iterate thru the linked list, and put the values into the tmp list
            tmp = []
            while head:
                  tmp.append(head.val)
                  head = head.next

            # Create the res as a linked list
            res = ListNode()
            # Set a tmp node which is pointing to the head first
            current = res
            tmp.reverse()
            for i in range(len(tmp)):
                  if i == len(tmp)-1: # cuz the last element doesn't need to create a next node
                        current.val = tmp[i]
                  else: # assign the val to the node; create a next node; set the tmp node to the next node
                        current.val = tmp[i]
                        current.next = ListNode()
                        current = current.next

            # output the answer
            return res
