# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # Remove the N-th node from the end
        left.next = left.next.next
        
        # Return the head of the modified list
        return dummy.next