from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Include the current number
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude the current number and all it's duplicates'
            subset.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            dfs(i)

        dfs(0)

        return res
