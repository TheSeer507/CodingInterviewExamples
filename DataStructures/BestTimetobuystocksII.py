#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

#On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

#Find and return the maximum profit you can achieve.

#Approach - We start with a variable profit that is what we need to calculate
#After we use a for loop to go through the array of prices
#We compare if prices in a certain array position is greater than the previous position
#if so we increase our profit by deducting the price of the last transaction
#we return the profit after loop is complete

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]
                profit += (prices[i] - prices[i-1])
        return profit