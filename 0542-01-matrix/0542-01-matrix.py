class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1

        # Multi-source BFS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                        mat[nr][nc] = dist
                        q.append((nr, nc))

            dist += 1
        
        return mat



                