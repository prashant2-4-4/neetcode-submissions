"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        has_map = {}
        #first pass create a new node

        curr = head
        while curr:
            has_map[curr] = Node(curr.val)
            curr = curr.next
        
        #now store this the next node
        curr = head
        while curr:
            if curr.next:
                has_map[curr].next = has_map[curr.next]
            
            if curr.random:
                has_map[curr].random = has_map[curr.random]
        
            curr = curr.next
        
        return has_map[head]  if head else None