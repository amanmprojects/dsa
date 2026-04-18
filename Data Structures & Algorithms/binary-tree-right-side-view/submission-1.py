class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([root])
        res = [root.val]
        
        while queue:
            q_new = deque([])
            for q in queue:
                if q.left:
                    q_new.append(q.left)
                if q.right:
                    q_new.append(q.right)
            if q_new:
                right_most = q_new[-1]
                res.append(right_most.val)
            queue = q_new
        
        return res