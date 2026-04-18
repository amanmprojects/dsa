class Solution:
    def countWaysRec(self, n: int, dp: List[int]):
        if n == 0 or n == 1:
            return 1

        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.countWaysRec(n-1, dp) + self.countWaysRec(n-2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)

        return self.countWaysRec(n, dp)
