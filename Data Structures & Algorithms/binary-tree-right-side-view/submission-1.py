# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        out = []
        while queue:
            level_size = len(queue)
            # level = []
            for i in range(level_size):
                node = queue.popleft()
                # level.append(node.val)
                if i ==level_size -1 :
                    out.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            # out.append(level[-1])
        
        return out

        
        