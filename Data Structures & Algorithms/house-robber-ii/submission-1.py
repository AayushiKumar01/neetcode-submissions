class Solution:
    def rob(self, nums: List[int]) -> int:
        set1 = nums[1:]
        set2 = nums[:-1]

        rob1= rob2 = 0
        set1_max = 0
        set2_max = 0

        for num in set1:
            set1_max = max(rob1+num,rob2)
            rob1 = rob2
            rob2 = set1_max
        
        rob1= rob2 = 0
        for num in set2:
            set2_max = max(rob1+num,rob2)
            rob1 = rob2
            rob2 = set2_max
        
        return max(nums[0],set1_max,set2_max)

        