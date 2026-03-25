from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Rule 1: must have n-1 edges
        if len(edges) != n - 1:
            return False

        # Build undirected graph
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        # Start from node 0
        if not dfs(0, -1):
            return False

        # Check if all nodes are connected
        return len(visit) == n
