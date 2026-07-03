class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        q = deque([])
        visit = set()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))

        # Multi-source BFS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visit:
                        visit.add((nr, nc))
                        mat[nr][nc] = dist
                        q.append((nr, nc))

            dist += 1
        
        return mat



                