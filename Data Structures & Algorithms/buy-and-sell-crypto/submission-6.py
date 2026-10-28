class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0

        for r in range(len(prices)):
            while prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res

