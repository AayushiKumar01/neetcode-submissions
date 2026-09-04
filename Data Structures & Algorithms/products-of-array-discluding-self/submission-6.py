class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res[i] = prod
        # return res
        numsProd = 1
        zero_count = 0
        
        for i in range(len(nums)):
            if nums[i]:
                numsProd *= nums[i]
            else:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            if zero_count:
                if nums[i]:
                    res[i] = 0
                else:
                    res[i] = numsProd
            else:
                res[i] = numsProd // nums[i]
        return res