from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            u, v = words[i], words[i + 1]

            # to get until which character are they similar
            j = 0
            while j < min(len(u), len(v)) and u[j] == v[j]:
                j += 1

            # for the case that one word is prefix of another
            if j == min(len(u), len(v)):
                # Wierd / Impossible ordering
                if len(v) < len(u):
                    return ""

                continue

            if u[j] in adj:
                adj[u[j]].add(v[j])

        res = []
        path = set()
        visited = set()

        def dfs(node: str):
            nonlocal res

            # If node in path i.e. cycle detected
            if node in path:
                return False

            if node in visited:
                return True

            # if has children, then dfs on them
            path.add(node)
            for child in adj[node]:
                if not dfs(child):
                    return False

            res.append(node)
            visited.add(node)
            path.remove(node)

            return True

        for c in adj:
            if c not in visited:
                if not dfs(c):
                    return ""
        res = ''.join(res)
        return res[::-1]
