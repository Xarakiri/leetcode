class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]

            profit = max(profit, price - cur_min)
            cur_min = min(cur_min, price)

        return profit
