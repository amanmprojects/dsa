class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        rd, cd = 0, 1
        visited = set()
        r, c = 0, 0 

        for _ in range(ROWS * COLS):
            res.append(matrix[r][c])
            visited.add((r, c))


            nr, nc = r + rd, c + cd

            if (nr, nc) in visited or nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                match (rd, cd):
                    case (0, 1): # Left
                        rd, cd = 1, 0
                    case (1, 0): # Down
                        rd, cd = 0, -1
                    case (0, -1): # Right
                        rd, cd = -1, 0
                    case (-1, 0): # Up
                        rd, cd = 0, 1
                    
                
                nr, nc = r + rd, c + cd

            r, c = nr, nc

        return res