class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # edge case
        n = len(nums)
        if n == 2:
            return [1,2]

        '''
        scan to get a b
        a <- index of first nonneg number
        b <- index of first number greater than target
        
        res = [-1, -1]
        for i in range(len(nums)):
            key = target-nums[i]

            if i < a:
                lo, hi = 0, a-1
            elif i < b: 
                lo, hi = a, b-1
            else:
                lo, hi = b, n-1
            
            j = bin_search(key, nums, lo, hi)
            if j != -1:
                res = [i+1,j+1]
                break

        return res

        algorithm bin_search(key, nums, lo, hi):
            if lo == hi:
                return -1
            
            mid = lo+hi // 2
            if nums[mid] == key:
                return mid
            elif nums[mid] < key:
                return bin_search(key, nums, lo, mid)
            elif nums[mid] > key:
                return bin_search(key, nums, mid+1, hi)
        '''

        def bin_search(key:int, nums: List[int], lo: int, hi: int):
            # base case
            if lo > hi:
                return -1
            
            # recursive case
            mid = (lo+hi) // 2
            print([lo, mid, hi])
            if key == nums[mid]:
                return mid
            elif key > nums[mid]:
                return bin_search(key, nums, mid+1, hi) 
            elif key < nums[mid]:
                return bin_search(key, nums, lo, mid-1)

        res = [-1, -1]
        for i in range(n):
            x, y = nums[i], target-nums[i]
            j = bin_search(y, nums, 0, n-1)
            if j != -1:
                res = [i+1,j+1]
                break

        return res
