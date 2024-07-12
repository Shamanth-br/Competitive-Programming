class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy,sell = prices[0],prices[0]
        for price in prices:
            if price > sell:
                sell = price

            elif price < buy:
                buy = price
                sell = price
            profit = max(profit,sell-buy)
        return profit
        