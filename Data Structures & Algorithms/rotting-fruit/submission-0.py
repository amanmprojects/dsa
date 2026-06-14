class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        time = 0
        while fresh != 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    rn, rc = r + dr, c + dc

                    if rn in range(R) and rc in range(C) and grid[rn][rc] == 1:
                        fresh -= 1
                        grid[rn][rc] = 2
                        q.append((rn, rc))
            print(fresh, q)
            time += 1
        
        if fresh == 0:
            return time
        
        return -1

