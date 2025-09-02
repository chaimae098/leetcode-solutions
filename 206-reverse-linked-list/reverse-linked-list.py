from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional['Node'] = None

class Solution:
    def __init__(self):
        self.head: Optional[Node] = None

    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        prev = None
        current = head

        while current:
            nxt = current.next     
            current.next = prev   
            prev = current         
            current = nxt          

        return prev  
