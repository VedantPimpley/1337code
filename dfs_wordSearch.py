from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        l = len(word)

        def dfs(r: int, c: int, idx: int) -> bool:
            # base cases
            ## found word - all letters found
            if idx == l:
                return True

            ## out of bounds
            if r < 0 or c < 0 or r > m-1 or c > n-1:
                return False

            ## letter mismatch
            if board[r][c] != word[idx]:
                return False

            ## recursive case
            tmp = board[r][c]
            board[r][c] = '#'
            found = (
                dfs(r+1, c, idx+1) or
                dfs(r-1, c, idx+1) or
                dfs(r, c+1, idx+1) or
                dfs(r, c-1, idx+1)
            )
            board[r][c] = tmp

            return found
        
        # driver
        for r in range(m):
            for c in range(n):
                res = dfs(r, c, 0)
                if res:
                    return True
        return False