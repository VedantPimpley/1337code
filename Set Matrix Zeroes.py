class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        requires:
            matrix is non-empty
        ensures:
            forall.r in m.c in n. 
                if matrix[r][c] == 0 then matrix'[r][0..c] == 0 and matrix'[0..r][c] == 0
        algo:
            zerod_rows = [False] * n
            zerod_cols = [False] * m
            
            for r,c in zip(range(0,m), range(0,n)):
                if matrix[r][c] == 0:
                    zerod_rows[r] = True
                    zerod_cols[c] = True
            
            for r in range(0, m): #scanning rows
                if zerod_rows[r]:
                    for c in range(0, n):
                        matrix[r][c] = 0

            for c in range(0, n): #scanning cols
                if zerod_cols[c]:
                    for r in range(0, m):
                        matrix[r][c] = 0
            
            return matrix
        '''

        # edge case
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n == 1:
            return matrix
        
        # general case
        zerod_rows = [False] * m
        zerod_cols = [False] * n
        
        for r in range(0,m): #scanning all cells
            for c in range(0,n):
                if matrix[r][c] == 0:
                    zerod_rows[r] = True
                    zerod_cols[c] = True
                print((r,c))
        
        for r in range(0, m): #scanning rows
            if zerod_rows[r]:
                for c in range(0, n):
                    matrix[r][c] = 0

        for c in range(0, n): #scanning cols
            if zerod_cols[c]:
                for r in range(0, m):
                    matrix[r][c] = 0