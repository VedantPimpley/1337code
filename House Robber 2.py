class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        requires:
            len(nums) >= 1
            all values in nums are >= 0
        ensures:
            res is max, aware of circular list
        algo:
            n == 0 -> nums[0]

            
        '''

        n = len(nums)
        # edge case
        if n == 1:
            return nums[0]

        # general case
        def rob_linear(numbers:list[int]) -> int:
            m = len(numbers)
            f = {i: None for i in range(m)}
            f[-1], f[-2] = 0, 0
            
            for i in range(m):
                f[i] = max(f[i-1], f[i-2] + numbers[i])

            return f[m-1]

        res = max(rob_linear(nums[1:]), rob_linear(nums[:n-1]))
        return res