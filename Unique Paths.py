class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        y = f(cell) = number of ways you can reach cell from (0,0)

        transition = no of ways received from above-cell and from left-cell

        base case = f(0,0) = 1 

        dp : dict[(i,j), no_of_ways]. v init to 0.

        order: asc_i, asc_j

        pass self to lower-cell and right-cell. increment.

        answer: dp(m-1, n-1)
        '''

        # edge case
        if m == 1 and n == 1:
            return 1

        # general case
        dp: dict[tuple[int,int], int] = {}
        dp = {(i,j): 0 for i in range(m) for j in range(n)} # init as 0
        print(dp)
        dp[(0,0)] = 1 # base case

        for i in range(m):
            for j in range(n):
                own_val = dp[(i,j)]
                assert own_val != 0 # sanity check
                lower_cell_k, right_cell_k = (i, j+1), (i+1, j)
                if lower_cell_k in dp:
                    dp[lower_cell_k] += own_val
                if right_cell_k in dp:
                    dp[right_cell_k] += own_val

        return dp[(m-1,n-1)]

                
