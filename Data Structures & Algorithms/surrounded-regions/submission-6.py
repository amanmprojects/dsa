class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or r >= R) or (c < 0 or c >= C) or board[r][c] != "O":
                return

            board[r][c] = "#"
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for c in range(C):
            dfs(0, c)
            dfs(R-1, c)

        for r in range(1, R-1):
            dfs(r, 0)
            dfs(r, C-1)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"


        

    
            
                        

