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
        # numsProd = 1
        # zero_count = 0
        
        # for i in range(len(nums)):
        #     if nums[i]:
        #         numsProd *= nums[i]
        #     else:
        #         zero_count += 1
        # if zero_count > 1:
        #     return [0] * len(nums)
        
        # res = [0] * len(nums)

        # for i in range(len(nums)):
        #     if zero_count:
        #         if nums[i]:
        #             res[i] = 0
        #         else:
        #             res[i] = numsProd
        #     res[i] = numsProd // nums[i]
        # return res


        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
