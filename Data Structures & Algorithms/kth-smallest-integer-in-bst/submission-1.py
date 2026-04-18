class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = []

        while curr is not None:
            stack.append(curr)
            curr = curr.left
        
        k_curr = 1
        res = 0
        while k_curr <= k:
            top = stack.pop()
            res = top.val

            if top.right:
                stack.append(top.right)
                top = top.right
                while top.left:
                    stack.append(top.left)
                    top = top.left
            
            k_curr += 1

        return res