class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        requires (i):
            at least one land tile must exist (else return 0)
            at least one water tile must exist (else return 1)
            grid must be non-empty
        ensures:
            output >= 2
        algo:
            VARS
                isl_ct
                unvisited
                cur
                next
                nei

            unvisited: set = all the land tiles
            isl_ct = 0

            while unvisited
                isl_ct += 1

                cur = {unvisited.pop()}
                while cur:
                    next = {}
                    for land in cur:
                        nei = get_unv_land_nei(land)
                        
                        next |= nei
                        unvisited -= nei
                    cur = next
            return isl_ct
        '''

        m, n = len(grid), len(grid[0])
        land = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == '1']
        # edge cases
        # if land:
        #     return 0
        # if len(land) == m*n: # no water
        #     return 1

        # general case
        unvisited: set[tuple[int,int]] = set(land)
        isl_ct: int = 0

        while unvisited:
            isl_ct += 1

            cur: set[tuple[int,int]] = { unvisited.pop() }
            while cur:
                nxt: set[tuple[int,int]] = set()
                for land in cur:
                    nei = set()
                    i, j = land
                    for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                        if x in range(0,m) and y in range(0,n) and grid[x][y] == '1' and (x,y) in unvisited:
                            nei.add((x,y))
                    
                    nxt |= nei
                    unvisited -= nei
                cur = nxt
        
        return isl_ct
                
