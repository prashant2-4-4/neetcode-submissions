# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_same(node , subRoot):
            if not node and not subRoot:
                return True

            if not node or not subRoot:
                return False

            if node.val != subRoot.val:
                return False
            
            if check_same(node.left , subRoot.left) and check_same(node.right , subRoot.right):
                return True


            return False
            
        
        def recursion(node):
            if not node:
                return False
            
            out = check_same(node , subRoot)
            # print(out , node.val)
            if out:
                return True
            if recursion(node.left):
                return True
            if recursion(node.right):
                return True
            return False
        return recursion(root)