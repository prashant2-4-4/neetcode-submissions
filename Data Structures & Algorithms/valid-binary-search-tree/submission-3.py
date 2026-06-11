# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node , range_val):
            if not node:
                return True
            
            if not range_val[0] < node.val < range_val[1]:
                return False
            
            return dfs(node.left , (range_val[0] , min(node.val , range_val[1]))) and dfs(node.right , (max(node.val , range_val[0]) , range_val[1]))            

            return True
            

        return dfs(root , (float("-inf") , float("inf")))
        