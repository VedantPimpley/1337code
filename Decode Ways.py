class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        requires:
            s != '0'
        ensures:
            res >= 1 if s is valid else 0
        algo: -
        '''
        

        # edge case
        if s[0] == '0':
            return 0
        
        n = len(s)
        dp = {n:1}

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
 
            if i <= n-2:
                pair = int(s[i]+s[i+1])
                if pair >= 10 and pair <= 26:
                    dp[i] += dp[i+2]

        return dp[0]