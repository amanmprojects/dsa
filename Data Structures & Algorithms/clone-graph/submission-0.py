from os import CLONE_FILES
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return

        visited = {}

        def dfs(node: Node):
            if node in visited:
                return visited[node]

            clone = Node(node.val)
            visited[node] = clone
            
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            
            return clone

        return dfs(node=node)
