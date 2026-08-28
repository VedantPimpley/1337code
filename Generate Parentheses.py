class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        open, to_open, buffer, res
            if to_open == 0 and open == 0:
                res.append(buffer)
            
            if open > 0:
                f(open-1, to_open, buffer + ")", res) #close
            if to_open > 0:
                f(open+1, to_open-1, buffer + "(", res) #open
        '''

        # edge case
        if n == 1:
            return ["()"]

        # general case
        def f(open_ct: int, to_open_ct: int, buffer: str, res: list[str]) -> None:
            # base case
            if to_open_ct == 0 and open_ct == 0:
                res.append(buffer)

            # recursive case
            if open_ct > 0:
                f(open_ct-1, to_open_ct, buffer + ")", res) #close
            if to_open_ct > 0:
                f(open_ct+1, to_open_ct-1, buffer + "(", res) #open

        res: list[str] = []
        f(0, n, "", res)

        return res