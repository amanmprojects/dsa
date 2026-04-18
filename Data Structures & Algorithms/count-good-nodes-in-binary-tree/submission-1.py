

class Solution:
        
    def goodNodes(self, root: TreeNode, maxParent: int = -101) -> int:
        node = root
        if not node: return 0
        return (0 if node.val < maxParent else 1) + self.goodNodes(node.left, max(maxParent, node.val)) + self.goodNodes(node.right, max(maxParent, node.val))
