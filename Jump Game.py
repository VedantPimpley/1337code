class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''

        [True] + [False] * n-1

        frontier = [0]

        while frontier:
            new_frontier = []
            for i in frontier:
                if nums[i] > 0:
                    new_frontier.append( i+nums[i] )
            frontier = [i for i in new_frontier if i < n]

        return reachable[n-1]

        '''

        n = len(nums)
        # edge cases
        if n == 1:
            return True
        if n == 2:
            return nums[0] == 1

        # general case
        reachable: list[bool] = [True] + [False for i in range(n)]
        frontier = [0]

        while frontier:
            new_frontier = []
            for i in frontier:
                if nums[i] > 0 and i+nums[i] < n: # then jump
                    new_frontier.append(i+nums[i])
                    reachable[i+nums[i]] = True
            frontier = new_frontier
            # print(nums)
            # print(reachable)
            # print(frontier)
            # print("\n")
            

        return reachable[n-1]

        