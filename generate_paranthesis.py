from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        open, close = 0, 0
        arr = []

        def dfs():
            nonlocal open, close
            if close > open:
                return

            if open > n:
                return

            if len(arr) >= n * 2:
                res.append("".join(arr))
                return

            arr.append("(")
            open += 1
            dfs()
            arr.pop()
            open -= 1

            arr.append(")")
            close += 1
            dfs()
            arr.pop()
            close -= 1

        dfs()

        return res
