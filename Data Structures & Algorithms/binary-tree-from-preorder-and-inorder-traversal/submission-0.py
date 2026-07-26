# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #inorder_map

        inorder_map = {value : i for i , value in enumerate(inorder)}
        # print(inorder_map)

        preorder_idx = 0

        def traversal(left , right):
            nonlocal preorder_idx

            if left > right:
                return None
            
            root_value = preorder[preorder_idx]
            preorder_idx += 1
        
            mid = inorder_map[root_value]

            root = TreeNode(root_value)

            root.left = traversal(left , mid-1)
            root.right = traversal(mid+1 , right)

            return root
        
        return traversal(0 , len(inorder)-1)