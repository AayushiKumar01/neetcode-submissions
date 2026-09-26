class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0, 1
        # maxProfit = 0
        # while (r < len(prices)):
        #     if prices[l] < prices[r]:
        #         diff = prices[r] - prices[l]
        #         maxProfit = max(maxProfit, diff)
        #     else:
        #         l = r
        #     r += 1
        # return maxProfit


        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            minPrice = min(price, minPrice)
            profit = price - minPrice
            maxProfit = max(profit, maxProfit)

        return maxProfit