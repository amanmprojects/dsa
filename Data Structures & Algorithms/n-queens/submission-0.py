from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [-1] * n
        colSet = set()
        posDiagSet = set()
        negDiagSet = set()

        def ok(r, c):
            if c in colSet:
                return False
            if r - c in posDiagSet:
                return False
            if r + c in negDiagSet:
                return False
            return True

        def dfs(i):
            if i >= n:
                res.append(board.copy())
                return

            for j in range(n):
                board[i] = j
                if ok(i, j):
                    colSet.add(j)
                    posDiagSet.add(i - j)
                    negDiagSet.add(i + j)
                    dfs(i + 1)
                    colSet.remove(j)
                    posDiagSet.remove(i - j)
                    negDiagSet.remove(i + j)

        dfs(0)

        print(res)
        resf = []
        for r in res:
            resf.append([])
            for i in range(n):
                s = ""
                for j in range(n):
                    if j == r[i]:
                        s += "Q"
                    else:
                        s += "."
                resf[-1].append(s)

        return resf
