from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        arr = []
        sum = 0

        def dfs(i):
            print(arr)
            nonlocal sum

            if sum > target:
                return

            if sum == target:
                res.append(arr.copy())
                return

            if i >= len(candidates):
                return

            arr.append(candidates[i])
            sum += candidates[i]
            dfs(i + 1)

            arr.pop()
            sum -= candidates[i]
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            dfs(i)

        dfs(0)

        return res
