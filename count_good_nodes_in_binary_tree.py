# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        
    def goodNodes(self, root: TreeNode, maxParent: int = -101) -> int:
        node = root
        if not node: return 0
        return (0 if node.val < maxParent else 1) + self.goodNodes(node.left, max(maxParent, node.val)) + self.goodNodes(node.right, max(maxParent, node.val))
