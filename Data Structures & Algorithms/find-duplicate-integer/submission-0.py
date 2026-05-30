class Node:
    def __init__(self , val):
        self.val =val
        self.next = None

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #using floyd algo and directly using index as one node and value as cycle node
        slow , fast = nums[0] , nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
        # head = Node(nums[0])
        # curr = head
        # for i in range(1 , len(nums)):
        #     curr.next = Node(nums[i])
        #     curr = curr.next

        # # created a linked list
        # #now implement floyd algo which say starting of cycle is
        # # where fast and slow meet and then second slow and old slow meet

        # fast = slow = second_slow = head

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         break
        
        # # now second iteration of slow and second_slow
        # while second_slow != slow:
            
        #     slow = slow.next
        #     second_slow = second_slow.next
        
        # return slow.val
        
        