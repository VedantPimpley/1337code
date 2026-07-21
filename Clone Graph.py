"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        requires:
            non null graph
            input node.val == 1
        ensures:
            -
        algo:
            cur: 'Node' = node
            q: set['Node'] = set(Node)
            visited: set['Node'] = set([]) 
            d: dict[int, 'Node'] = {}

            while q:
                cur = q.pop()
                d[cur.val] = Node(node.val)
                cl_cur = d[cur.val]
                for nd in cur.neighbors:
                    if nd.val not in d:
                        d[nd.val] = Node(nd.val)

                cl_cur.neighbors = [d[nd.val] for nd in cur.neighbors]

                visited |= cur
                q |= cur.neighbors - visited

            return d[1]

        '''

        # edge case
        if not node:
            return None

        # general case
        cur: 'Node' = node
        q: set['Node'] = set([node])
        visited: set['Node'] = set([])
        d: dict[int, 'Node'] = {}

        while q:
            cur = q.pop()
            d[cur.val] = d[cur.val] if cur.val in d else Node(cur.val)
            cl_cur = d[cur.val]

            for nd in cur.neighbors:
                if nd.val not in d:
                    d[nd.val] = Node(nd.val)
            cl_cur.neighbors = [d[nd.val] for nd in cur.neighbors]

            visited |= set([cur])
            q |= set(cur.neighbors) - visited

        return d[1]