"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

def maxProfit(prices):
    profit = 0
    start = 0

    for i in range(1, len(prices)):
        if prices[i] < prices[start]:
            start = i
        else:
            profit = max(prices[i] - prices[start], profit)
    return profit 


assert maxProfit([7,1,5,0,6,4]) == 6
assert maxProfit([3, 4, 1, 5, 6, 6, 4, 2]) == 5
assert maxProfit([7,1,5,3,6,4]) == 5
assert maxProfit([1, 2]) == 1