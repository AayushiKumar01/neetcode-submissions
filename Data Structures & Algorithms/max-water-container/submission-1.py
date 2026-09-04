class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):

        #         maxHeight = min (heights[i], heights[j])
        #         cap = (j - i) * maxHeight
        #         maxWater = max(cap, maxWater)

        # return maxWater

        l, r = 0, len(heights) - 1

        while l < r:
            maxHeight = min (heights[l], heights[r])
            cap = (r - l) * maxHeight
            maxWater = max(cap, maxWater)

            if heights[l] <= heights[r]:
                l +=  1
            else:
                r -= 1
        return maxWater

        