# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# level  based bfs , path based dfs

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node , max_so_far):
            if not node:
                return 0
            
            score = 1 if node.val >= max_so_far else 0
        
            new_max = max(max_so_far , node.val)

            return score + dfs(node.right , new_max) + dfs(node.left , new_max)

        
        return dfs(root , float("-inf"))
        