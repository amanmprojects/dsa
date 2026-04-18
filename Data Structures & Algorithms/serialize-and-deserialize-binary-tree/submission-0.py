# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "null"
        
        curr_val = root.val
        res = f"{curr_val}"

        return res + "," + self.serialize(root=root.left) + "," + self.serialize(root=root.right)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        
        def dfs() -> Optional[TreeNode]:
            curr_val = vals[self.i]
            
            if curr_val == "null":
                self.i += 1
                return None
            
            curr = TreeNode(int(vals[self.i]))
            self.i += 1
            curr.left = dfs()
            curr.right = dfs()

            return curr

        return dfs()
