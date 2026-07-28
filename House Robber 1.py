class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        requires:
            len(nums) > 1
            all values in nums are geq 0
        ensures:
            no consecutive houses will be picked
        algo:
            n == 1 -> nums[0]

            f_i = max(f_i-1, f_i-2 + nums[i])

            return f_n-1
        '''

        n = len(nums)
        # edge case
        if n == 1:
            return nums[0]

        # general case
        f = {i: None for i in range(n)}
        f[-1], f[-2] = 0, 0

        for i in range(n):
            f[i] = max(f[i-1], f[i-2] + nums[i])

        return f[n-1]