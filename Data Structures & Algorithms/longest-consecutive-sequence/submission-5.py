class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longestSeq = 1
        seq = 1
        sortedNums = sorted(nums)
        for i in range(len(nums)-1):
            if sortedNums[i+1] - sortedNums[i] == 1:
                seq += 1
                longestSeq = max(longestSeq, seq)
            elif sortedNums[i+1] - sortedNums[i] == 0:
                continue
            else:
                seq = 1
        return longestSeq