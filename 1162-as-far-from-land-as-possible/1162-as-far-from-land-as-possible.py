class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        result = -1
        q = deque([])

        visit = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    q.append((r, c))
                    visit.add((r, c))
            
        # Multi-source BFS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 1:
                        grid[nr][nc] = 1
                        q.append((nr, nc))
                
            result += 1
        
        return result if result > 0 else -1

            

