from math import inf
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        memo = {}
        def dfs(s: int):
            if s in memo:
                return memo[s]
            if s > amount:
                return inf

            if s == amount:
                return 0   # 🔥 key fix
            
            m = inf
            for c in coins:
                m = min(m, 1 + dfs(s + c))
            
            memo[s] = m
            
            return m
        
        res = dfs(0)
        return res if res != inf else -1