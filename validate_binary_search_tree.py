from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], min: int = None, max: int = None) -> bool:
        if root is None: return True 

        if max and not min:
            if root.val > max: return False
            return self.isValidBST(root.left, max = root.val) and self.isValidBST(root.right, max=max, min=root.val)
        if min and not max:
            if root.val < min: return False
            return self.isValidBST(root.right, min=root.val) and self.isValidBST(root.left, min=min, max=root.val)
        if min and max:
            if root.val < min or root.val > max: return False
            return self.isValidBST(root.left, max=root.val, min=min) and self.isValidBST(root.right, min=root.val, max=max)
        return self.isValidBST(root.left, max=root.val) and self.isValidBST(root.right, min=root.val)