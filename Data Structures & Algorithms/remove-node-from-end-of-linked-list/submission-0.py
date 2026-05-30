# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count total len
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        
        from_start = count - n
        start = 0
        ans = head

        if from_start == 0:
            return head.next

        while ans:
            if start==from_start-1:
                ans.next = ans.next.next
                break
            ans = ans.next
            start += 1
        
        return head

        