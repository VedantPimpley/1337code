class Solution:
    def climbStairs(self, n: int) -> int:
        # y - no of ways to climb.. to reach step s

        # f(step s) = y

        # f(1) = 1
        # f(2) = 2
        # f(3) = f(2) + f(1)
        # f(s) = f(s-1) + f(s-2)

        dp = {1: 1, 2:2}
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
