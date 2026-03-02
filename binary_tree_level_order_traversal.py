from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    res = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        elif(root.left is None and root.right is None): return [[root.val]]
        res = []                                                       
        q = deque([root])
        exp = 0
        c = 1
        curr_depth = 0
        while q:
            curr = q.popleft()
            if len(res) <= curr_depth: res.append([])
            res[curr_depth].append(curr.val)
            if (curr.left): q.append(curr.left)
            if(curr.right): q.append(curr.right)
            if(c % (2**exp) == 0): 
                curr_depth += 1
                exp += 1
            c += 1

        return res         

        

