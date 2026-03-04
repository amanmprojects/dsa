from typing import Optional, List, Deque
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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


            
                
