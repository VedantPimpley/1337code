class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        requires:
            * grid is non-empty
        ensures:
            * if no 0s -> return grid
            * all land cells will have the least distance to a chest
            * all land cells will contain [1, INF]
        algo:

        epoch
        seed
        just_visited
        next_unv_nei
        infi = 2147483647

            get_unv_nei(grid, i, j) -> list[tuple]
                res = set()
                for r,c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                    if r in range(m) and c in range(n) and grid[r][c] == infi:
                        res.add((r,c))
                return res

            m, n = len(grid), len(grid[0])
            epoch = 0
            seed = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 0]
            just_visited = seed
            while just_visited:
                epoch += 1

                next_unv_nei = set()
                for cell in just_visited:
                    next_unv_nei |= get_unv_nei(cell)
                for cell in next_unv_nei:
                    grid[cell[0]][cell[1]] = epoch
                
                just_visited = next_unv_nei
            return epoch

        '''

        # edge case
        m, n = len(grid), len(grid[0])
        treasure = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 0]
        if not treasure:
            return grid

        # general case
        infi = 2147483647
        just_visited = treasure
        epoch = 0
        while just_visited:
            epoch += 1

            to_visit = set()
            for i,j in just_visited:
                unv_nei = set()
                for r,c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if r in range(m) and c in range(n) and grid[r][c] == infi:
                        unv_nei.add((r,c))
                to_visit |= unv_nei
            for r,c in to_visit:
                grid[r][c] = epoch
            just_visited = to_visit