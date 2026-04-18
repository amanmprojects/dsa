# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countGoodNodes(self, node: TreeNode, maxParent: int):
        if not node: return 0
        return (0 if node.val < maxParent else 1) + self.countGoodNodes(node.left, max(maxParent, node.val)) + self.countGoodNodes(node.right, max(maxParent, node.val))
        
    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.countGoodNodes(root.left, root.val) + self.countGoodNodes(root.right, root.val)