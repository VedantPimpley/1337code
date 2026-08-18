class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m,n = len(board), len(board[0])
        # edge cases
        if m == 1 and n == 1: #single-tile board
            return
        if m == 1 or n == 1: #row/col board
            return

        # general case
        Os = [(i,j) for i in range(m) for j in range(n) if board[i][j] == 'O']
        external_Os = [(i,j) for i,j in Os if i == 0 or i == m-1 or j == 0 or j == n-1]
        unreached_internal_Os = set(Os) - set(external_Os)

        for tile in external_Os:
            region = {tile}
            while region:
                pos = region.pop()

                r,c = pos
                nei = {
                    (x,y) for x,y in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)] 
                        if x in range(m) 
                        and y in range(n) 
                        and (x,y) in unreached_internal_Os
                }

                region |= nei
                unreached_internal_Os -= nei

        for i,j in unreached_internal_Os:
            board[i][j] = 'X'