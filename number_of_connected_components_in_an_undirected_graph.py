from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        for u, v in edges:
            if u not in adj:
                adj[u] = set()
            if v not in adj:
                adj[v] = set()
            adj[u].add(v)
            adj[v].add(u)

        visited = set()

        def dfs(node, parent):
            if node not in visited:
                visited.add(node)
                if node in adj:
                    for nei in adj[node]:
                        dfs(nei, node)

        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1

        return count
