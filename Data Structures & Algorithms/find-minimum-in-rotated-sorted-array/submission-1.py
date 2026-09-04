class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1

        min_val = float('infinity')

        while l <= r:
            mid = (l+r) // 2
            if nums[r] <= nums[mid]:
                l = mid + 1
            else:
                r = r-1
            min_val = min(min_val, nums[mid])
        return min_val
        