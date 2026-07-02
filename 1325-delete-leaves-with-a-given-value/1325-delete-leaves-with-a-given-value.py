# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(n):
            if n is None:
                return 

            n.left = dfs(n.left)
            n.right = dfs(n.right)

            if n.left is None and n.right is None and n.val == target:
                return None
            
            return n

        return dfs(root)
