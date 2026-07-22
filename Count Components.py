class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        requires:
            n >= 2
        ensures:
            res < n
        algo:
            construct a graph using edges, represented using a dict
            maintain a set unvisited = {0..n-1}
            init res = 0
            pick any value from unvisited, run bfs till no unvisited neighbors left, increment res
            keep doing this unvisited is empty
        '''


        # edge case
        if n == 2:
            return 1

        # general case
        d: dict[int, set[int]] = {}
        for i in range(n):
            d[i] = set([])
        for i,j in edges:
            d[i].add(j)
            d[j].add(i)
        
        unvisited : set[int]= set([x for x in range(n)])
        res = 0
        while unvisited:
            res += 1

            seed = unvisited.pop()
            unv_nei: set[int] = d[seed] & unvisited
            while unv_nei and unvisited:
                nd = unv_nei.pop()
                unvisited.remove(nd)
                unv_nei |= (d[nd] & unvisited)

        return res
