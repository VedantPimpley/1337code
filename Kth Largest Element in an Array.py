class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        heapify nums into a max-heap
        heap-pop() k-1 elements
        return heap-pop() for kth largest element
        '''

        import heapq
        
        h = [-x for x in nums]
        heapq.heapify(h)
        
        i = 1
        while i < k:
            heapq.heappop(h)
            i += 1
        kth_largest = -heapq.heappop(h)
        return kth_largest