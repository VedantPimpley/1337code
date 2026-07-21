class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        requires:
            grid is non-empty
        ensures:
            if no 2s -> return -1
            if no 1s -> return 0

            at any minute,  if no new cells were rotten -> return -1
        algo:
            propogation based approach

            track fresh
            at every minute, 
                in every adj cell of fresh
                if any fresh exist, make them rotten
                trck in new-state
        '''
        m, n = len(grid), len(grid[0])
        fresh = set([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        rotting = set([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 2])

        # edge cases
        if not fresh:
            return 0
        if not rotting:
            return -1

        # general case
        minute = 0
        while fresh:
            minute += 1

            newly_rotten = set([])
            for i,j in rotting:
                for r,c in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if r in range(m) and c in range(n):
                        if grid[r][c] == 1:
                            grid[r][c] = 2
                            newly_rotten.add((r,c))

            if not newly_rotten:
                return -1
            else:
                fresh -= newly_rotten
                rotting = newly_rotten

        return minute
            