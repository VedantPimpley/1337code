class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        requires:
            * len(s) >= 1
        ensures:
            * len(output) >= 1
        algo:
            res = ("",0)
            dp: list[int] = [True for _ in range(n)]
            for i in range(n, -1, -1):
                for j in range(n, i-1, -1):
                    dp[j] = (dp[j-1] and s[i] == s[j]) if i != j else (s[i], 1)
                    if dp[i] and j-i > res[1]:
                        res = (s[i:j+1], j-i)
            return res[0]
        '''

        # edge case
        n = len(s)
        if n == 1:
            return s

        # general case
        res = ("", 0)
        dp = [[False for _ in range(n)] for __ in range(n)]
        for i in reversed(range(n)):
            for j in range(i,n):
                l = j-i+1
                inner_string_pal = dp[i+1][j-1] if j-i >= 3 else True
                ends_match = s[i] == s[j]
                if ends_match and inner_string_pal:
                    dp[i][j] = True
                    if l > res[1]:
                        res = (s[i:j+1], l)
        return res[0]