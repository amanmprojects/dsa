from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If preorder is empty means no children to add
        if len(preorder) == 0:
            return None
        
        # If preorder contains only one element then no need to recurse
        if len(preorder) == 1:
            return TreeNode(val=preorder[0], left=None, right=None)
        
        # Value for current Node
        curr_value = preorder[0]

        # Remove the current value from preorder
        preorder.remove(curr_value)

        # Find where the current value lies in the inorder, elements on left go to left subtree, and elements on right go to right subtree
        mid = inorder.index(curr_value)

        # Create the current node with current value
        curr = TreeNode(curr_value)

        # Calculate the lenght (no. of nodes) of left subtree to slice preorder into left and right parts
        len_left = mid

        # Add the children
        curr.left = self.buildTree(preorder=preorder[:len_left], inorder=inorder[:mid])
        curr.right = self.buildTree(preorder=preorder[len_left:], inorder=inorder[mid+1:])

        return curr