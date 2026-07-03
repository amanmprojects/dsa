class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque([entrance])
        maze[entrance[0]][entrance[1]] = '+'
        dist = 0
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r in [0, m-1] or c in [0, n-1]:
                    if [r, c] != entrance:
                        return dist
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                        maze[nr][nc] = '+'
                        q.append((nr, nc))
            dist += 1
        return -1

