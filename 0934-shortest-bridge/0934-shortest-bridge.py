class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # Queue to store all points of first island, to do multi-source bfs later
        q = deque()
        
        found = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    found = True
                    break
            if found:
                break
            
        # Temporary queue for first BFS
        tq = deque([(r, c)])
        q.append((r, c))
        grid[r][c] = -1
        
        # BFS to find all points of first island
        while tq:
            for _ in range(len(tq)):
                r, c = tq.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 1:
                        grid[nr][nc] = -1
                        q.append((nr, nc))
                        tq.append((nr, nc))
        
        # Finally we have all points of first island, now we need to do multi-source bfs from all these points

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc] != -1:
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = -1
                            q.append((nr, nc))
                        elif grid[nr][nc] == 1:
                            return dist
                
            dist += 1

        return -1
                        
                



