from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        count = 0
        arr = []
        sum = 0
        def dfs(i):
            
            nonlocal sum
            print(arr)
            
            if i >= len(nums):
                return
            
            # Base Case
            if sum > target:
                return
                
            # Found a result
            if sum == target:
                res.append(arr.copy())
                return 
                
            arr.append(nums[i])
            sum += nums[i]
            dfs(i)
            
            arr.pop()
            sum -= nums[i]
            dfs(i+1)
        
        dfs(0)
            
        return res