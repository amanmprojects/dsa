class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        safe = [[False for col in range(C)] for row in range(R)]

        def dfs(r, c):
            if (r >= 0 and r < R) and (c >=0 and c < C) and board[r][c] == "O":
                if safe[r][c]:
                    return

                safe[r][c] = True
                
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for c in range(C):
            dfs(0, c)
            dfs(R-1, c)

        for r in range(R):
            dfs(r, 0)
            dfs(r, C-1)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O" and not safe[r][c]:
                    board[r][c] = "X"

    
            
                        

