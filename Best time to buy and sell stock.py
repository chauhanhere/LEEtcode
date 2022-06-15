def maxProfit(prices: list[int]) -> int:
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit,min_price

a,b=maxProfit([7,1,5,3,6,4])
print('Buying the stock on day',b,'and Selling the stock on day',a,'will give maximum profit')
