class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            # Base Case: Valid permutation
            if i >= len(s):
                return 1
            
            res = 0
            
            # Take next one letter
            if self.isValid(s[i]):
                res += dfs(i+1)

            # Take two letters if exist
            if i < len(s)-1:
                if self.isValid(s[i:i+2]):
                    res += dfs(i+2)
            
            memo[i] = res
            return res
        
        return dfs(0)
    
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        if s[0] == '0':
            return False

        if len(s) == 1:
            return True
        
        if len(s) == 2:
            if int(s) > 26:
                return False
            return True
            
        return False



        
