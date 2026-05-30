# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        ans = curr
        carry = 0
        while l1 or l2:
            if l1 and l2:
                v = l1.val + l2.val + carry
                l1 = l1.next 
                l2 = l2.next
            elif l1:
                v = l1.val + carry
                l1 = l1.next
            else:
                v = l2.val + carry
                l2 = l2.next
            
            curr.next = ListNode(v%10)
            carry = v//10
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        
        return ans.next


        