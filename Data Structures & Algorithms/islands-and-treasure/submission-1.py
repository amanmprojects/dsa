class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        INF = 2147483647

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r,c))


        distance = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            distance += 1
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    rn, cn = r+dr, c+dc
                    if rn in range(R) and cn in range(C) and grid[rn][cn] == INF:
                        grid[rn][cn] = distance
                        q.append((rn, cn))
        
