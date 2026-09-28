class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        robbed_money = 0

        for num in nums:
            robbed_money = max(prev1,prev2+num)
            prev2=prev1
            prev1 = robbed_money
        
        return robbed_money
        