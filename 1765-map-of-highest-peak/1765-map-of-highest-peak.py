class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        m, n = len(isWater), len(isWater[0])
        heights = isWater

        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    q.append((r, c))
                    heights[r][c] = 0
                else:
                    heights[r][c] = -1
        print(heights)
                
        # Multi Source
        directions = [(0,1),(0, -1), (1, 0), (-1,0)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] == -1:
                        heights[nr][nc] = heights[r][c] + 1
                        q.append((nr, nc))

        return heights

    