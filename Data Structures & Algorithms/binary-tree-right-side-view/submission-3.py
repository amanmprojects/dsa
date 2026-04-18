class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []
        
        while q:
            qLen = len(q)

            for i in range(qLen):
                curr = q.popleft()
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            
            res.append(curr.val)
        
        return res