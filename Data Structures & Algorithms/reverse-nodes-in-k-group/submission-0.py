# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            check = group_prev
            for i in range(k):
                check = check.next
                # handle the end
                if not check:
                    return dummy.next

            #reverse the node
            prev = None
            curr = group_prev.next
            tail = curr # direction of last
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            #connect with previous group
            group_prev.next = prev
            tail.next = curr

            group_prev = tail
        
        return dummy.next





        



        