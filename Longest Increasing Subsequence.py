class TrieNode:
    def __init__(self, val: int, depth: int, nxt = None):
        self.val = val
        self.depth = depth
        self.nxt = nxt

class Solution:
    def old_lengthOfLIS(self, nums: List[int]) -> int:
        '''
        requires:
            len(nums) > 1
        ensures:
            len(out) >= 1
        algo:
            trie(v, nxt, l)
            root(-1001, 0, None)
            out = 0
            leaves = {root}
            for x in nums:
                new_leaves = {root}
                for nd in leaves:
                    if nd.val < x:
                        leaves |= {trie(x, nd.l+1)}
                        out = max(out, nd.l+1)
            return out
        '''

        n = len(nums)

        # edge case
        if n == 1:
            return 1

        # general case
        root = TrieNode(-1001, 0)
        out = 0
        leaves = {root}
        for x in nums:
            new_leaves = set()
            for nd in leaves:
                if nd.val < x:
                    new_nd = TrieNode(x, nd.depth+1)
                    new_leaves.add(new_nd)
                    out = max(out, new_nd.depth)
            leaves |= new_leaves
        return out

    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        requires:
            * len(nums) > 1
        ensures:
            * out >= 1
        algo:
            f_i = 1 (base case)
                  1 + max(dp[j]) for all j in [0,i] where nums[i] > nums[j]

            dp = [1 for _ in range(n)]

            for i in range(n):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j])
            
            return max(dp[i])
        '''

        n = len(nums)
        # edge case
        if n == 1:
            return 1

        # general case
        dp: list[int] = [1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)