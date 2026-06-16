class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        borderOs = []
        safe = [[False for col in range(C)] for row in range(R)]
        visited = set()

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    if r in [0, R-1] or c in [0, C-1]:
                        borderOs.append((r, c))

        def dfs(r, c):
            if (r >= 0 and r < R) and (c >=0 and c < C) and board[r][c] == "O":
                if safe[r][c]:
                    return

                safe[r][c] = True
                
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for r, c in borderOs:
            dfs(r, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O" and not safe[r][c]:
                    board[r][c] = "X"

    
            
                        

