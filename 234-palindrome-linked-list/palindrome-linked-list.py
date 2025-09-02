# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        L =[]
        pos = 0
        currentNode = head
        while currentNode :
            L.append(currentNode.val) 
            currentNode = currentNode.next
            pos +=1
        for i in range(int(pos/2)):
            if L[i]!=L[pos-i-1]:
                return False
        return True        

