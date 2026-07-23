class LRUCache:
    '''
    LRUCache data structure
    requires:
        * capacity > 0
    ensures:    
        put(k, v) -> None
        * overwrites existing v if any
        * deletes LRU k:v pair if len' = capacity+1
        * moves k to most recently used status
        * o(1)
        get(k) -> v
        * returns val v associated with key k
        * returns -1 if k is not present in the data structure
        * moves k to most recently used status
        * o(1)
    algo:

        2 sentinel nodes
        head and tail
        deletions from tail pred_k
        put/get moves key to head succ_k

        head_nd - nodes - tail_nd
        each node := has pred_k:int, succ_k:int, val:int
        head = LRUNode(None, None, None)
        tail = LRUNode(None, None, None)

        class LRUNode:
            def __init__(val:int, pred_k:int = None, succ_k:int = None):
                self.val = val
                self.pred_k = pred_k
                self.succ_k = succ_k

        put
            if l == cap and k not in d:
                delete last node
            if l < cap and k in d:
                l += 1

            if k in d and cap avlb -> delete existing
            if k not in d

            # fresh addition
            # fresh addition - not full - just add new, incr length
            # fresh addition - full - delete last and add new, incr length
            

            # existing updation
            # existing updation - delete existing, add new

        get
            # absent
            return -1

            # present - remove existing, add it back
    '''

    class LRUNode:
        def __init__(self, val:int, pred_k:int = None, succ_k:int = None):
            self.val = val
            self.pred_k = pred_k
            self.succ_k = succ_k

    def __init__(self, capacity: int):
        self.cap = capacity
        self.l = 0
        
        self.d: dict[LRUNode] = {}
        head_nd = self.LRUNode(val=None,succ_k=-2) #-1 is head
        tail_nd = self.LRUNode(val=None,pred_k=-1) #-2 is tail
        self.d[-1] = head_nd
        self.d[-2] = tail_nd

    def _remove_nd(self, k) -> None:
        assert k in self.d

        this_nd = self.d[k]
        pred_nd = self.d[this_nd.pred_k]
        succ_nd = self.d[this_nd.succ_k]

        pred_nd.succ_k = this_nd.succ_k
        succ_nd.pred_k = this_nd.pred_k
        del self.d[k]
        self.l -= 1

    def get(self, k: int) -> int:
        if k not in self.d:
            return -1

        v = self.d[k].val
        self.put(k, v)

        return v
        
    def put(self, k: int, v: int) -> None:
        # remove lru if we're already at capacity and fresh k is being added
        if self.l == self.cap and k not in self.d:
            lru_nd_k = self.d[-2].pred_k
            self._remove_nd(lru_nd_k)

        # remove existing entry if k already exists
        if k in self.d:
            self._remove_nd(k)

        # add new value
        head_nd = self.d[-1]
        first_nd = self.d[head_nd.succ_k]
        new_nd = self.LRUNode(val=v, succ_k=head_nd.succ_k, pred_k=-1)
        self.d[k] = new_nd
        head_nd.succ_k = k
        first_nd.pred_k = k
        self.l += 1