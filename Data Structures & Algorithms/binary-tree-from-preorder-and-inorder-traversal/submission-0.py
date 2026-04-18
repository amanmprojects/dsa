
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(val=preorder[0], left=None, right=None)
        
        curr_value = preorder[0]
        preorder.remove(curr_value)

        mid = inorder.index(curr_value)

        curr = TreeNode(curr_value)

        len_left = mid
        len_right = len(inorder)-1-mid

        curr.left = self.buildTree(preorder=preorder[:len_left], inorder=inorder[:mid])
        curr.right = self.buildTree(preorder=preorder[len_left:], inorder=inorder[mid+1:])

        return curr