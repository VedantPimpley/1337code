class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        requires:
            piles is not empty
            h >= length of piles
        ensures:
            res <= max(piles)
            (res-1) * h < sum(piles)
        '''

        n = len(piles)
        # edge case
        if n == h:
            return max(piles)

        # general case
        s = sum(piles)
        lo = math.ceil(s/h)
        hi = max(piles)
        mi = (lo+hi)//2

        print(f's {s}')
        while lo <= hi:
            mi = (lo+hi) // 2

            timeTaken = 0
            for p in piles:
                timeTaken += math.ceil(p/mi)
            if timeTaken <= h:
                res = mi # best solution yet
                hi = mi-1
            else:
                lo = mi+1
            
        return res