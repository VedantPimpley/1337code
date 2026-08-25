class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        requires (i):
            * edges represents a graph G with n edges and n nodes (1 thru n)
            * G has a cycle in it
        ensures:
            * output represents an edge that will create a cycle in G if added
        algo:
            visited = {}

            for a,b in edges:
                #1
                v = {1,2}
                #2
                v = {1,2,3}
                #3
                v = {1,2,3,4}
                #4 !! => Both are in visited. [1,4] is redundant.
                v = {1,2,3,4}
                #5
                v = {1,2,3,4,5}
                
                #1
                v = {1,2}
                #2
                v = {1,2,3}
                #3
                v = {1,2,3,4}
                #4 !! => Both are in visited. [2,4] is redundant.

                [1,2], [1,3], [1,4], [2,3]
                #1
                v = {1,2}
                #2
                v = {1,2,3}
                #3
                v = {1,2,3,4}
                #4 !! => both are in visited. [2,3] is redundant.


            init visited: set[int] = {}
            out = None
            for a,b in edges:
                if a in edges and b in edges:
                    out = [a,b]
                else:
                    edges.add(a)
                    edges.add(b)
            return out

        '''

        n = len(edges)
        parent_lookup = {i:i for i in range(n + 1)}

        def find(x: int, parent_lookup: dict) -> int:
            while x != parent_lookup[x]:
                x = parent_lookup[x]
            return x
        
        out = [None, None]

        for e in edges:
            a, b = e
            r_a, r_b = find(a, parent_lookup), find(b, parent_lookup) # find of union-find
            if r_a == r_b: 
                # a and b were already connected, this e now creates a loop
                return e
            parent_lookup[r_a] = r_b # union of union-find
        return out