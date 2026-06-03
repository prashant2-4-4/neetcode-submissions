# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(node1 , node2):
            if not node1 and not node2:
                return 1
            
            if not node1 or not node2:
                return -1

            if check(node1.left , node2.left) == -1:
                return -1
           
            if check(node1.right , node2.right) == -1:
                return -1
            
            
            if node1.val == node2.val:
                return 1
            
            else:
                return -1

        
        return check(p , q) != -1
        