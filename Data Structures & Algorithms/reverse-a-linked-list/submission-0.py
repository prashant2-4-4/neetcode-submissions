# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         Original:  1 → 2 → 3 → 4 → None

# Step 1:  None ← 1   2 → 3 → 4
# Step 2:  None ← 1 ← 2   3 → 4
# Step 3:  None ← 1 ← 2 ← 3   4
# Step 4:  None ← 1 ← 2 ← 3 ← 4
        prev = None
        curr = head

        while curr:
            next_node = curr.next #save curr before breaking
            curr.next = prev # break it
            prev = curr
            curr = next_node

        
        return prev
        