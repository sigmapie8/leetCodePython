class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10001
        max_profit = 0
        for index, price in enumerate(prices):
            if(price < buy):
                buy = price
            elif(price-buy > max_profit):
                max_profit = price - buy
        return max_profit
